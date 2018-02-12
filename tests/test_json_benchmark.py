# vim: set fileencoding=utf-8 sw=4 et tw=79
import mixedmartialtail
import pytest
import io
from mock import patch
from test_variables import *

@pytest.mark.benchmark(
    min_rounds=5,
)

@pytest.mark.idparametrize('input,expected_syslog,expected_json', test_parameters)
def test_json_one_line(capsys, benchmark, input, expected_syslog, expected_json):
    with patch.object(mixedmartialtail, 'get_input', return_value=io.StringIO(input)):
        benchmark(mixedmartialtail.main, argv=[])
    out, err = capsys.readouterr()
    assert out == expected_syslog
    assert err == ""
