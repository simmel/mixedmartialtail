#!/usr/bin/env python3
# vim: set fileencoding=utf-8 sw=4 et tw=79

import mixedmartialtail
import re
import json

@mixedmartialtail.hookimpl()
def apply(line):
    first = line.find("{")
    last = line.rfind("}")
    if first != -1 and last != -1:
        j = json.loads(line[first:last+1])
        return u"{}{}{}".format(line[0:first], j['message'], line[last+1:])
