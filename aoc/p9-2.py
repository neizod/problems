#!/usr/bin/env python3

import re


def extract_garbages(stream):
    return re.findall(r'<((?:!.|[^>])*)>', stream)


def count_garbages(stream):
    return sum(len(re.sub(r'!.', '', garbage)) for garbage in extract_garbages(stream))


def main():
    print(count_garbages(input().strip()))


if __name__ == '__main__':
    main()
