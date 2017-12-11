#!/usr/bin/env python3


def twist(ls, t):
    return ls[t:] + list(reversed(ls[:t]))


def solve(size, ts):
    skip = 0
    index = 0
    ls = list(range(size))
    for t in ts:
        ls = twist(ls, t)
        ls = ls[skip:] + ls[:skip]
        index += t + skip
        index %= len(ls)
        skip += 1
        skip %= len(ls)
    return ls[-index:] + ls[:-index]


def main():
    ts = [int(n) for n in input().split(',')]
    ls = solve(256, ts)
    print(ls[0] * ls[1])


if __name__ == '__main__':
    main()
