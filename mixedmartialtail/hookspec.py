#!/usr/bin/env python3
# vim: set fileencoding=utf-8 sw=4 et tw=79
import pluggy

hookspec = pluggy.HookspecMarker('mixedmartialtail.plugins')

@hookspec(firstresult=True)
def match(line):
    """Check if the log line matches the formats we can handle

    :param line: Line to check if it matches our format
    :type line: String
    """
    pass

@hookspec(firstresult=True)
def apply(line):
    """Apply our format to the line

    :param line: Line to apply format to
    :type line: String
    """
    pass
