#!/usr/bin/env python3

from operator import xor
from functools import reduce


def twist(ls, t):
    return ls[t:] + list(reversed(ls[:t]))


def solve(size, ts, nos_rounds=1):
    skip = 0
    index = 0
    ls = list(range(size))
    for _ in range(nos_rounds):
        for t in ts:
            ls = twist(ls, t)
            ls = ls[skip:] + ls[:skip]
            index += t + skip
            index %= len(ls)
            skip += 1
            skip %= len(ls)
    return ls[-index:] + ls[:-index]


def xor_hash(ls):
    return [reduce(xor, ls[16*i:16*(i+1)]) for i in range(len(ls)//16)]


def hexify(dense):
    return ''.join('{:02x}'.format(n) for n in dense)


def main():
    ts = [ord(n) for n in input().strip()] + [17,31,73,47,23]
    sparse = solve(256, ts, 64)
    dense = xor_hash(sparse)
    print(hexify(dense))


if __name__ == '__main__':
    main()
