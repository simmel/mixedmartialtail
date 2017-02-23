#!/usr/bin/env python3
# vim: set fileencoding=utf-8 sw=4 et tw=79

import mixedmartialtail
import re
import json

prog = re.compile(r"(.*?)({.*})(.*?)")

@mixedmartialtail.hookimpl()
def match(line):
    if "{" in line:
        return True
    else:
        return None

@mixedmartialtail.hookimpl()
def apply(line):
    if match(line):
        apa = prog.match(line)
        if apa:
            j = json.loads(apa.group(2))
            return "{}{}{}".format(apa.group(1), j['message'], apa.group(3))
