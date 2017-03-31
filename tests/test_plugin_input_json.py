# vim: set fileencoding=utf-8 sw=4 et tw=79
import mixedmartialtail
from mock import patch
import io
import json
import pytest

syslog = u'2005-04-12T17:03:45.000Z sarena.waza.se '
message = u'''🔣This is a log message🆒, there's no other like it.㊙️'''
log4j2_json = u'''{{"timeMillis":1487684052412,"thread":"main","level":"INFO","loggerName":"App","message":"{message}","endOfBatch":false,"loggerFqcn":"org.apache.logging.log4j.spi.AbstractLogger","threadId":1,"threadPriority":5}}'''.format(message=message)
logback_json = u'''{{"timestamp":"2005-04-12 17:03:45.000","level":"ERROR","thread":"Main","logger":"root","message":"{message}"}}'''.format(message=message)
log4j_jsonevent_layout = u'''{{"class":"org.eclipse.jetty.examples.logging.EchoFormServlet","@version":1,"source_host":"sarena.waza.se","thread_name":"qtp513694835-14","message":"{message}","@timestamp":"2014-01-27T19:52:35.738Z","level":"INFO","file":"EchoFormServlet.java","method":"doPost","logger_name":"org.eclipse.jetty.examples.logging.EchoFormServlet"}}'''.format(message=message)
logstashV0 = u'''{{"@fields":{{"levelname":"WARNING","name":"root","process":1819,"processName":"MainProcess","threadName":"MainThread"}},"@message":"{message}","@source_host":"sarena.waza.se","@timestamp":"2013-05-02T09:39:48.013158"}}'''.format(message=message)
logstashV1 = u'''{{"@version":1,"filename":"test.py","@timestamp":"2015-03-30T09:46:23.000Z","threadName":"MainThread","process":10787,"source_host":"sarena.waza.se","processName":"MainProcess","name":"root","levelname":"WARNING","message":"{message}"}}'''.format(message=message)

test_parameters = {
        # https://logging.apache.org/log4j/2.x/manual/layouts.html#JSONLayout
        'log4j2': (
            u'{syslog}{json_log}\n'.format(syslog=syslog, json_log=log4j2_json),
            u'{syslog}{message}\n'.format(syslog=syslog, message=json.loads(log4j2_json)['message']),
        ),
        # https://github.com/qos-ch/logback-contrib/wiki/JSON
        'logback': (
            u'{syslog}{json_log}\n'.format(syslog=syslog, json_log=logback_json),
            u'{syslog}{message}\n'.format(syslog=syslog, message=json.loads(logback_json)['message']),
        ),
        # https://github.com/logstash/log4j-jsonevent-layout
        'log4j-jsonevent-layout': (
            u'{syslog}{json_log}\n'.format(syslog=syslog, json_log=log4j_jsonevent_layout),
            u'{syslog}{message}\n'.format(syslog=syslog, message=json.loads(log4j_jsonevent_layout)['message']),
        ),
        # Logstash V0
        # https://github.com/logstash/logstash-logback-encoder
        # https://github.com/ulule/python-logstash-formatter
        # FIXME Enable after adding find_message_field
        # 'logstashV0': (
            # u'{syslog}{json_log}\n'.format(syslog=syslog, json_log=logstashV0),
            # u'{syslog}{message}\n'.format(syslog=syslog, message=json.loads(logstashV0)['@message']),
        # ),
        # Logstash V1
        # https://github.com/ulule/python-logstash-formatter
        'logstashV1': (
            u'{syslog}{json_log}\n'.format(syslog=syslog, json_log=logstashV1),
            u'{syslog}{message}\n'.format(syslog=syslog, message=json.loads(logstashV1)['message']),
        ),
    }

@pytest.mark.idparametrize('input,expected', test_parameters)
def test_json_uses_correct_message(capsys, input, expected):
    with patch.object(mixedmartialtail, 'get_input', return_value=io.StringIO(input)):
        mixedmartialtail.main(argv=[])
    out, err = capsys.readouterr()
    assert out == expected
    assert err == ""
