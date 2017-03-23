#!/usr/bin/env python3
# vim: set fileencoding=utf-8 sw=4 et tw=79
import pluggy

hookspec = pluggy.HookspecMarker('mixedmartialtail.plugins.input')

@hookspec(firstresult=True)
def apply(line, args):
    """Apply our format to the line

    :param line: Line to apply format to
    :type line: String

    :param args: argparse parsed arguments
    :type line: Namespace
    """
    pass

@hookspec()
def add_argument(parser):
    """Add argparse arguments

    :param parser: argparse parser
    :type parser: ArgumentParser
    """
    pass
