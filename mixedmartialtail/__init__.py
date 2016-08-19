#!/usr/bin/env python3
# vim: set fileencoding=utf-8 sw=4 et tw=79
import sys
import io

def main():
    from pkg_resources import iter_entry_points

    available_plugins = []
    for entry_point in iter_entry_points(group='mixedmartialtail.plugins', name=None):
        available_plugins.append(entry_point.load())

    input = io.open(sys.stdin.fileno(), 'r', encoding='utf-8', errors='replace')
    for line in input:
        if available_plugins[0].match(line):
            sys.stdout.write(available_plugins[0].apply(line))

if __name__ == "__main__":
    main()
