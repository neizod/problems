#!/usr/bin/env python3

import re


def is_nice(word):
    if not re.search(r'(..).*\1', word):
        return False
    if not re.search(r'(.).\1', word):
        return False
    return True


def main():
    try:
        count = 0
        while True:
            word = input().strip()
            count += is_nice(word)
    except EOFError:
        print(count)


if __name__ == '__main__':
    main()
