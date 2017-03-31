# vim: set fileencoding=utf-8 sw=4 et tw=79
# From https://mail.python.org/pipermail/pytest-dev/2013-June/002295.html
# https://gist.github.com/pfctdayelise/5719730
def pytest_generate_tests(metafunc):
    """
    If the test_ fn has a idparametrize mark, use it to create parametrized
    tests with ids. Instead of giving a list of argvals (test values), it
    should be a dict of test id strings -> tuple of test values
    e.g.
    @pytest.mark.idparametrize(('a', 'b'), {
        'foo': (1, 2),
        'bar': (3, 4),
    })
    """

    idparametrize = getattr(metafunc.function, 'idparametrize', None)
    if idparametrize:
        argnames, testdata = idparametrize.args
        ids, argvalues = zip(*sorted(testdata.items()))
        metafunc.parametrize(argnames, argvalues, ids=ids)
