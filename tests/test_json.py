# vim: set fileencoding=utf-8 sw=4 et tw=79
import mixedmartialtail
from mock import patch
import io

def test_cat_deals_with_utf8(capsys):
    with patch.object(mixedmartialtail, 'get_input', return_value=io.StringIO(u'dat 💩\n')):
        mixedmartialtail.main(argv=[])
    out, err = capsys.readouterr()
    assert out == u"dat 💩\n"
    assert err == ""
