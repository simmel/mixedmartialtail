#!/usr/bin/env python3
# vim: set fileencoding=utf-8 sw=4 et tw=79
import sys
import io

def main():
    input = io.open(sys.stdin.fileno(), 'r', encoding='utf-8', errors='replace')
    for line in input:
        sys.stdout.write(line)

if __name__ == "__main__":
    main()
