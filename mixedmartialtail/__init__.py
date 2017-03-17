#!/usr/bin/env python3
# vim: set fileencoding=utf-8 sw=4 et tw=79
import sys
import io
import pluggy
from . import hookspec

hookimpl = pluggy.HookimplMarker('mixedmartialtail.plugins.input')

def main():
    pm = pluggy.PluginManager('mixedmartialtail.plugins.input')
    pm.add_hookspecs(hookspec)
    pm.load_setuptools_entrypoints('mixedmartialtail.plugins.input')

    input = io.open(sys.stdin.fileno(), 'r', encoding='utf-8', errors='replace')
    for line in input:
        formatted = pm.hook.apply(line=line)
        if formatted:
            sys.stdout.write(formatted)
        else:
            raise NotImplementedError("This line cannot be parsed by any plugin:", line)

if __name__ == "__main__":
    main()
