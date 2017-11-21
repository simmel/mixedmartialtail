#!/usr/bin/env python3
# vim: set fileencoding=utf-8 sw=4 et tw=79
import sys
import io
import pluggy
from . import hookspec
import argparse
from signal import signal, SIGPIPE, SIG_DFL

# Use the default handler for SIGPIPE since the Python default to ignore it
# using SIG_IGN doesn't seem make it catchable via BrokenPipeError
signal(SIGPIPE,SIG_DFL)

hookimpl = pluggy.HookimplMarker('mixedmartialtail.plugins.input')

def get_input():
    return io.open(sys.stdin.fileno(), 'r', encoding='utf-8', errors='replace')

def main(argv=sys.argv[1:]):
    pm = pluggy.PluginManager('mixedmartialtail.plugins.input')
    pm.add_hookspecs(hookspec)
    pm.load_setuptools_entrypoints('mixedmartialtail.plugins.input')

    parser = argparse.ArgumentParser()
    pm.hook.add_argument(parser=parser)
    args = parser.parse_args(argv)

    try:
        for line in get_input():
            formatted = pm.hook.apply(line=line, args=args)
            if formatted:
                sys.stdout.write(formatted)
                sys.stdout.flush()
            else:
                raise NotImplementedError("This line cannot be parsed by any plugin:", line)
    except (KeyboardInterrupt):
        pass

if __name__ == "__main__":
    main()
