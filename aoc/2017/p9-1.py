#!/usr/bin/env python3

import re


def calc_score(stream):
    score = 0
    depth = 0
    for c in remove_garbages(stream):
        if c == '{':
            depth += 1
            score += depth
        if c == '}':
            depth -= 1
    return score


def remove_garbages(stream):
    return re.sub(r'<(!.|[^>])*>', '', stream)


def main():
    print(calc_score(input().strip()))


if __name__ == '__main__':
    main()
