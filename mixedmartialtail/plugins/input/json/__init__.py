#!/usr/bin/env python3
# vim: set fileencoding=utf-8 sw=4 et tw=79

import mixedmartialtail
import re
import json

@mixedmartialtail.hookimpl()
def apply(line, args):
    first = line.find("{")
    last = line.rfind("}")
    if first != -1 and last != -1:
        j = json.loads(line[first:last+1])
        if should_we_replace_the_line(args, first, last, line):
            return u"{}{}".format(find_message_field(j), line[last+1:])
        else:
            return u"{}{}{}".format(line[0:first], find_message_field(j), line[last+1:])

@mixedmartialtail.hookimpl()
def add_argument(parser):
    parser.add_argument("-i", "--replace-line",
            action="store_true",
            help="Force to replace the whole line, not just the part that's JSON.",)

def find_message_field(log=None):
    if "message" in log:
       return log["message"]
    elif "@message" in log:
       return log["@message"]
    elif "msg" in log:
       return log["msg"]
    else:
       raise NotImplementedError("Can't find message field in:", log)

def should_we_replace_the_line(args=None, first=None, last=None, line=None):
    # Replace if either:
    # * argument is given on command line
    # * there is nothing before or after the JSON
    return args.replace_line or (first == 0 and last+2 == len(line))
