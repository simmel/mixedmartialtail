# vim: set fileencoding=utf-8 sw=4 et tw=79
import mixedmartialtail
from mock import patch
import io
import json
import pytest

syslog = u'2005-04-12T17:03:45.000Z sarena.waza.se '
message = u'''🔣This is a log message🆒, there's no other like it.㊙️'''
log4j2_json = u'''{{"timeMillis":1487684052412,"thread":"main","level":"INFO","loggerName":"App","message":"{message}","endOfBatch":false,"loggerFqcn":"org.apache.logging.log4j.spi.AbstractLogger","threadId":1,"threadPriority":5}}'''.format(message=message)

test_parameters = {
        # https://logging.apache.org/log4j/2.x/manual/layouts.html#JSONLayout
        'log4j2': (
            u'{syslog}{json_log}\n'.format(syslog=syslog, json_log=log4j2_json),
            u'{syslog}{message}\n'.format(syslog=syslog, message=json.loads(log4j2_json)['message']),
        ),
    }

@pytest.mark.idparametrize('input,expected', test_parameters)
def test_json_uses_correct_message(capsys, input, expected):
    with patch.object(mixedmartialtail, 'get_input', return_value=io.StringIO(input)):
        mixedmartialtail.main(argv=[])
    out, err = capsys.readouterr()
    assert out == expected
    assert err == ""
