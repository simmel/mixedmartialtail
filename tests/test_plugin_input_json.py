# vim: set fileencoding=utf-8 sw=4 et tw=79
import mixedmartialtail
from mock import patch
import io
import pytest
import time
from test_variables import *

@pytest.mark.idparametrize('input,expected', test_parameters)
def test_json_uses_correct_message(capsys, input, expected):
    with patch.object(mixedmartialtail, 'get_input', return_value=io.StringIO(input)):
        mixedmartialtail.main(argv=[])
    out, err = capsys.readouterr()
    assert out == expected
    assert err == ""

def test_replace_line(capsys):
    with patch.object(mixedmartialtail, 'get_input', return_value=io.StringIO(u'''{"@fields":{"levelname":"WARNING","name":"root","process":1819,"processName":"MainProcess","threadName":"MainThread"},"@message":"🔣I'm not alone 🆒 I'll wait 'till the end of time for you.㊙️","@source_host":"sarena.waza.se","@timestamp":"2013-05-02T09:39:48.013158"}\n''')):
        mixedmartialtail.main(argv=["-i"])
    out, err = capsys.readouterr()
    assert out == u'''2013-05-02T09:39:48.013158{} root[1819]: WARNING 🔣I'm not alone 🆒 I'll wait 'till the end of time for you.㊙️\n'''.format(time.strftime("%z"))
    assert err == ""

def test_broken_json_and_stops(capsys):
    with patch.object(mixedmartialtail, 'get_input', return_value=io.StringIO(u'''{"@fields":{"@message": "🔣 dat broken"}''')):
        with pytest.raises(ValueError) as e:
            mixedmartialtail.main(argv=[])
    out, err = capsys.readouterr()
    assert out == ''
    assert err == ''

def test_broken_json_and_continues(capsys):
    with patch.object(mixedmartialtail, 'get_input', return_value=io.StringIO(u'{"message":"First working", "timestamp":"2013-05-02T09:39:48.013158"}\n{"@fields":{"@message": "🔣 dat broken"}\n{"message":"Last working", "timestamp":"2013-05-02T09:39:48.013158"}\n')):
        mixedmartialtail.main(argv=['-f'])
    out, err = capsys.readouterr()
    tz = time.strftime("%z")
    assert out == u'2013-05-02T09:39:48.013158{} First working\n{{"@fields":{{"@message": "🔣 dat broken"}}\n2013-05-02T09:39:48.013158{} Last working\n'.format(tz, tz)
    assert err == ''
