#!/usr/bin/env python3
# vim: set fileencoding=utf-8 sw=4 et tw=79
import sys
import io
import pluggy
from . import hookspec
import importlib

hookimpl = pluggy.HookimplMarker('mixedmartialtail.plugins')

def main():
    from pkg_resources import iter_entry_points

    pm = pluggy.PluginManager('mixedmartialtail.plugins')
    pm.add_hookspecs(hookspec)
    pm.load_setuptools_entrypoints('mixedmartialtail.plugins')

    input = io.open(sys.stdin.fileno(), 'r', encoding='utf-8', errors='replace')
    for line in input:
        if pm.hook.match(line=line):
            sys.stdout.write(pm.hook.apply(line=line))
        else:
            raise NotImplementedError("This line cannot be parsed by any plugin:", line)

if __name__ == "__main__":
    main()
