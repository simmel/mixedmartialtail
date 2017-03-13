#!/usr/bin/env python3
# vim: set fileencoding=utf-8 sw=4 et tw=79

import mixedmartialtail

@mixedmartialtail.hookimpl(trylast=True)
def apply(line):
    return line
