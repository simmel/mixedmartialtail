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
        return u"{}{}{}".format(line[0:first], find_message_field(j), line[last+1:])

def find_message_field(log=None):
    if "message" in log:
       return log["message"]
    elif "@message" in log:
       return log["@message"]
    elif "msg" in log:
       return log["msg"]
    else:
       raise NotImplementedError("Can't find message field in:", log)
