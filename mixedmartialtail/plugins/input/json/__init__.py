#!/usr/bin/env python3
# vim: set fileencoding=utf-8 sw=4 et tw=79

import mixedmartialtail
import re
import json
from datetime import datetime
from dateutil import parser, tz

@mixedmartialtail.hookimpl()
def apply(line, args):
    first = line.find("{")
    last = line.rfind("}")
    if first != -1 and last != -1:
        try:
            j = json.loads(line[first:last+1])
        except ValueError as e:
            if args.force:
                return None
            else:
                raise e
        if should_we_replace_the_line(args, first, last, line):
            return u"{}{}{}".format(create_prefix(j), find_message_field(j), line[last+1:])
        else:
            return u"{}{}{}".format(line[0:first], find_message_field(j), line[last+1:])

@mixedmartialtail.hookimpl()
def add_argument(parser):
    parser.add_argument("-i", "--replace-line",
            action="store_true",
            help="Force to replace the whole line, not just the part that's JSON.",)
    parser.add_argument("-f", "--force",
            action="store_true",
            help="Force to continue even if the plugins parsers are failing.",)

def find_message_field(log=None):
    if "message" in log:
       return log["message"]
    elif "@message" in log:
       return log["@message"]
    elif "msg" in log:
       return log["msg"]
    else:
       raise NotImplementedError("Can't find message field in:", log)

def create_prefix(log=None):
    """
    * Find the datetime
    * Find prog name
    * Find any log level
    * Return it all
    """
    prog = find_prog_field(log)
    pid = find_pid_field(log)
    level = find_level_field(log)
    return u'{} {}{}'.format(
            format_date(find_date_field(log)),
            u'{}{}{}'.format(
                prog if prog is not None else u'',
                u'[{}]'.format(pid) if pid is not None else u'',
                u': ' if prog is not None else u'',
            ),
            u'{} '.format(level) if level is not None else u'',
            )

def find_date_field(log=None):
    if "timestamp" in log:
       return log["timestamp"]
    elif "@timestamp" in log:
       return log["@timestamp"]
    elif "time" in log:
       return log["time"]
    elif "timeMillis" in log:
       return log["timeMillis"]
    elif "t" in log:
       return log["t"]
    elif "log_timestamp" in log:
       return log["log_timestamp"]
    else:
       raise NotImplementedError("Can't find date field in:", log)

def find_prog_field(log=None):
    """
    This is messier than usual. So many fields and it all depends on how you
    configure your logger:
    * thread
    * logger
    * class
    * file(name)
    * process(name)

    For now let's go with logger name because that's seems to be consistent
    over all loggers, so far.
    """
    if "loggerName" in log:
       return log["loggerName"]
    elif "logger" in log:
       return log["logger"]
    elif "logger_name" in log:
       # These are in a dotted form and we're only interested in the last bit.
       # E.g: "org.eclipse.jetty.examples.logging.EchoFormServlet"
       return log["logger_name"].split('.')[-1]
    elif "name" in log:
       return log["name"]
    elif "@fields" in log and "name" in log["@fields"]:
       return log["@fields"]["name"]
    elif "log_app" in log:
       return log["log_app"]
    else:
       pass

def find_pid_field(log=None):
    if "process" in log:
       return log["process"]
    elif "@fields" in log and "process" in log["@fields"]:
       return log["@fields"]["process"]
    elif "pid" in log:
       return log["pid"]
    else:
       pass

def find_level_field(log=None):
    if "level" in log:
       return log["level"]
    elif "levelname" in log:
       return log["levelname"]
    elif "@fields" in log and "levelname" in log["@fields"]:
       return log["@fields"]["levelname"]
    elif "log_level" in log:
       return log["log_level"]
    elif "lvl" in log:
       return log["lvl"]
    elif "severity" in log:
       return log["severity"]
    else:
       pass

def format_date(date=None):
    if type(date) is int:
        date = datetime.fromtimestamp(date/1000.0)
    elif date.isdigit():
        date = datetime.fromtimestamp(int(date)/1000.0)
    else:
        date = parser.parse(date, fuzzy=True)
    # If there's no TZ in the date, let's use the current one
    if date.tzinfo is None:
        date = date.replace(tzinfo=tz.tzlocal())
    return date.strftime("%FT%T.%f%z")

def should_we_replace_the_line(args=None, first=None, last=None, line=None):
    # Replace if either:
    # * argument is given on command line
    # * there is nothing before or after the JSON
    return args.replace_line or (first == 0 and last+2 == len(line))
