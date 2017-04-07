# vim: set fileencoding=utf-8 sw=4 et tw=79
import json
import time

syslog = u'2005-04-12T17:03:45.000Z sarena.waza.se '
message = u'''🔣This is a log message🆒, there's no other like it.㊙️'''
log4j2_json_json = u'''{{"timeMillis":1487684052412,"thread":"main","level":"INFO","loggerName":"App","message":"{message}","endOfBatch":false,"loggerFqcn":"org.apache.logging.log4j.spi.AbstractLogger","threadId":1,"threadPriority":5}}'''.format(message=message)
log4j2_json = json.loads(log4j2_json_json)
logback_json_json = u'''{{"timestamp":"2005-04-12 17:03:45.000","level":"ERROR","thread":"Main","logger":"root","message":"{message}"}}'''.format(message=message)
logback_json = json.loads(logback_json_json)
log4j_jsonevent_layout_json = u'''{{"class":"org.eclipse.jetty.examples.logging.EchoFormServlet","@version":1,"source_host":"sarena.waza.se","thread_name":"qtp513694835-14","message":"{message}","@timestamp":"2014-01-27T19:52:35.738Z","level":"INFO","file":"EchoFormServlet.java","method":"doPost","logger_name":"org.eclipse.jetty.examples.logging.EchoFormServlet"}}'''.format(message=message)
log4j_jsonevent_layout = json.loads(log4j_jsonevent_layout_json)
logstashV0_json = u'''{{"@fields":{{"levelname":"WARNING","name":"root","process":1819,"processName":"MainProcess","threadName":"MainThread"}},"@message":"{message}","@source_host":"sarena.waza.se","@timestamp":"2013-05-02T09:39:48.013158"}}'''.format(message=message)
logstashV0 = json.loads(logstashV0_json)
logstashV1_json = u'''{{"@version":1,"filename":"test.py","@timestamp":"2015-03-30T09:46:23.000Z","threadName":"MainThread","process":10787,"source_host":"sarena.waza.se","processName":"MainProcess","name":"root","levelname":"WARNING","message":"{message}"}}'''.format(message=message)
logstashV1 = json.loads(logstashV1_json)
json_log_formatter_json = u'''{{"message":"{message}","time":"2015-09-01T06:06:26.524448","referral_code":"52d6ce"}}'''.format(message=message)
json_log_formatter = json.loads(json_log_formatter_json)
json_logging_py_json = u'''{{"timestamp":"2015-09-22T22:40:56.178715Z","level":"ERROR","host":"sarena.waza.se","path":"example.py","message":"{message}","logger":"root"}}'''.format(message=message)
json_logging_py = json.loads(json_logging_py_json)
ougai_json = u'''{{"name":"main","hostname":"sarena.waza.se","pid":14607,"level":30,"time":"2016-10-16T22:26:48.835+09:00","v":0,"msg":"{message}"}}'''.format(message=message)
ougai = json.loads(ougai_json)
logstash_logger_json = u'''{{"message":"{message}","@timestamp":"2014-05-22T09:37:19.204-07:00","@version":"1","severity":"INFO","host":"sarena.waza.se"}}'''.format(message=message)
logstash_logger = json.loads(logstash_logger_json)
log_formatter_json = u'''{{"source":"sarena.waza.se","message":"{message}","log_level":"DEBUG","log_type":"Log4RTest","log_app":"app","log_timestamp":"2016-08-25T17:02:37+08:00"}}'''.format(message=message)
log_formatter = json.loads(log_formatter_json)
logrus_json = u'''{{"animal":"walrus","level":"info","msg":"{message}","size":10,"time":"2017-04-02T08:01:13+02:00"}}'''.format(message=message)
logrus = json.loads(logrus_json)
log15_json = u'''{{"answer":42,"lvl":0,"msg":"{message}","t":"2015-01-13T23:03:13.341434194+01:00"}}'''.format(message=message)
log15 = json.loads(log15_json)

test_parameters = {
        # https://logging.apache.org/log4j/2.x/manual/layouts.html#JSONLayout
        'log4j2': (
            u'{syslog}{json_log}\n'.format(syslog=syslog, json_log=log4j2_json_json),
            u'{syslog}{message}\n'.format(syslog=syslog, message=log4j2_json['message']),
            u'{date} {prog}: {level} {message}\n'.format(
                date=u'{}{}'.format(
                    '2017-02-21T14:34:12.412000',
                    time.strftime('%z'),
                ),
                prog=log4j2_json['loggerName'],
                level=log4j2_json['level'],
                message=log4j2_json['message'],
            ),
        ),
        # https://github.com/qos-ch/logback-contrib/wiki/JSON
        'logback': (
            u'{syslog}{json_log}\n'.format(syslog=syslog, json_log=logback_json_json),
            u'{syslog}{message}\n'.format(syslog=syslog, message=logback_json['message']),
            u'{date} {prog}: {level} {message}\n'.format(
                date=u'{}{}'.format(
                    logback_json['timestamp'],
                    time.strftime('%z'),
                ),
                prog=logback_json['logger'],
                level=logback_json['level'],
                message=logback_json['message'],
            ),
        ),
        # https://github.com/logstash/log4j-jsonevent-layout
        'log4j-jsonevent-layout': (
            u'{syslog}{json_log}\n'.format(syslog=syslog, json_log=log4j_jsonevent_layout_json),
            u'{syslog}{message}\n'.format(syslog=syslog, message=log4j_jsonevent_layout['message']),
            u'{date} {prog}: {level} {message}\n'.format(
                date=u'{}'.format(
                    log4j_jsonevent_layout['@timestamp'],
                ),
                prog=log4j_jsonevent_layout['logger_name'].split('.')[-1],
                level=log4j_jsonevent_layout['level'],
                message=log4j_jsonevent_layout['message'],
            ),
        ),
        # Logstash V0
        # https://github.com/logstash/logstash-logback-encoder
        # https://github.com/ulule/python-logstash-formatter
        'logstashV0': (
            u'{syslog}{json_log}\n'.format(syslog=syslog, json_log=logstashV0_json),
            u'{syslog}{message}\n'.format(syslog=syslog, message=logstashV0['@message']),
            u'{date} {prog}[{pid}]: {level} {message}\n'.format(
                date=u'{}{}'.format(
                    logstashV0['@timestamp'],
                    time.strftime('%z'),
                ),
                prog=logstashV0['@fields']['name'],
                pid=logstashV0['@fields']['process'],
                level=logstashV0['@fields']['levelname'],
                message=logstashV0['@message'],
            ),
        ),
        # Logstash V1
        # https://github.com/ulule/python-logstash-formatter
        'logstashV1': (
            u'{syslog}{json_log}\n'.format(syslog=syslog, json_log=logstashV1_json),
            u'{syslog}{message}\n'.format(syslog=syslog, message=logstashV1['message']),
            u'{date} {prog}[{pid}]: {level} {message}\n'.format(
                date=u'{}'.format(
                    logstashV1['@timestamp'],
                ),
                prog=logstashV1['name'],
                pid=logstashV1['process'],
                level=logstashV1['levelname'],
                message=logstashV1['message'],
            ),
        ),
        # https://github.com/marselester/json-log-formatter
        'json_log_formatter': (
            u'{syslog}{json_log}\n'.format(syslog=syslog, json_log=json_log_formatter_json),
            u'{syslog}{message}\n'.format(syslog=syslog, message=json_log_formatter['message']),
            u'{date} {message}\n'.format(
                date=u'{}'.format(
                    json_log_formatter['time'],
                ),
                message=json_log_formatter['message'],
            ),
        ),
        # https://github.com/sebest/json-logging-py
        'json_logging_py': (
            u'{syslog}{json_log}\n'.format(syslog=syslog, json_log=json_logging_py_json),
            u'{syslog}{message}\n'.format(syslog=syslog, message=json_logging_py['message']),
            u'{date} {prog}: {level} {message}\n'.format(
                date=u'{}'.format(
                    json_logging_py['timestamp'],
                ),
                prog=json_logging_py['logger'],
                level=json_logging_py['level'],
                message=json_logging_py['message'],
            ),
        ),
        # https://github.com/tilfin/ougai
        'ougai': (
            u'{syslog}{json_log}\n'.format(syslog=syslog, json_log=ougai_json),
            u'{syslog}{message}\n'.format(syslog=syslog, message=ougai['msg']),
            u'{date} {prog}[{pid}]: {level} {message}\n'.format(
                date=u'{}'.format(
                    ougai['time'],
                ),
                prog=ougai['name'],
                pid=ougai['pid'],
                level=ougai['level'],
                message=ougai['msg'],
            ),
        ),
        # https://github.com/dwbutler/logstash-logger
        'logstash_logger': (
            u'{syslog}{json_log}\n'.format(syslog=syslog, json_log=logstash_logger_json),
            u'{syslog}{message}\n'.format(syslog=syslog, message=logstash_logger['message']),
            u'{date} {level} {message}\n'.format(
                date=u'{}'.format(
                    logstash_logger['@timestamp'],
                ),
                level=logstash_logger['severity'],
                message=logstash_logger['message'],
            ),
        ),
        # https://github.com/chadlwm/log_formatter/
        'log_formatter': (
            u'{syslog}{json_log}\n'.format(syslog=syslog, json_log=log_formatter_json),
            u'{syslog}{message}\n'.format(syslog=syslog, message=log_formatter['message']),
            u'{date} {prog}: {level} {message}\n'.format(
                date=u'{}'.format(
                    log_formatter['log_timestamp'],
                ),
                prog=log_formatter['log_app'],
                level=log_formatter['log_level'],
                message=log_formatter['message'],
            ),
        ),
        # https://github.com/sirupsen/logrus
        'logrus': (
            u'{syslog}{json_log}\n'.format(syslog=syslog, json_log=logrus_json),
            u'{syslog}{message}\n'.format(syslog=syslog, message=logrus['msg']),
            u'{date} {level} {message}\n'.format(
                date=u'{}'.format(
                    logrus['time'],
                ),
                level=logrus['level'],
                message=logrus['msg'],
            ),
        ),
        # https://github.com/inconshreveable/log15
        'log15': (
            u'{syslog}{json_log}\n'.format(syslog=syslog, json_log=log15_json),
            u'{syslog}{message}\n'.format(syslog=syslog, message=log15['msg']),
            u'{date} {level} {message}\n'.format(
                date=u'{}'.format(
                    log15['t'],
                ),
                level=log15['lvl'],
                message=log15['msg'],
            ),
        ),
    }
