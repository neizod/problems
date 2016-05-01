#!/usr/bin/env python3

from collections import defaultdict


def populate(it, carry=''):
    if not it:
        yield carry
    elif it[0] != '?':
        yield from populate(it[1:], carry+it[0])
    else:
        for c in '0123456789':
            yield from populate(it[1:], carry+c)


def closest(score_a, score_b):
    poss_a = set(populate(score_a))
    poss_b = set(populate(score_b))
    result = defaultdict(list)
    for a in poss_a:
        for b in poss_b:
            result[abs(int(a) - int(b))] += [(a,b)]
    for key in sorted(result):
        for vals in sorted(result[key]):
            return vals


def main():
    for case in range(int(input())):
        print('Case #{}: {} {}'.format(case+1, *closest(*input().split())))


if __name__ == '__main__':
    main()
