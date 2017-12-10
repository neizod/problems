#!/usr/bin/env python3

from operator import xor
from functools import reduce


def twist(ls, index, size):
    if index+size <= len(ls):
        ls[index:index+size] = list(reversed(ls[index:index+size]))
    else:
        front = (index+size) % len(ls)
        split = len(ls) - index
        tmp = list(reversed(ls[index:]+ls[:front]))
        ls[index:] = tmp[:split]
        ls[:front] = tmp[split:]
    return ls


def solve(ts, nos_rounds=1):
    skip = 0
    index = 0
    ls = list(range(256))
    for _ in range(nos_rounds):
        for size in ts:
            ls = twist(ls, index, size)
            index += size + skip
            index %= len(ls)
            skip += 1
    return ls


def xor_hash(ls):
    return [reduce(xor, ls[16*i:16*(i+1)]) for i in range(16)]


def hexify(dense):
    return ''.join('{:02x}'.format(n) for n in dense)


def main():
    ts = [ord(n) for n in input().strip()] + [17,31,73,47,23]
    sparse = solve(ts, 64)
    dense = xor_hash(sparse)
    print(hexify(dense))


if __name__ == '__main__':
    main()
