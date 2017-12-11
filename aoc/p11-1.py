#!/usr/bin/env python3

from collections import Counter


def find_length(n, ne, nw):
    return sum(sorted([abs(n), abs(ne), abs(nw)], reverse=True)[:2])


def reduce_direction(moves):
    count = Counter(moves)
    n = count['n'] - count['s']
    ne = count['ne'] - count['sw']
    nw = count['nw'] - count['se']
    return find_length(n, ne, nw)


def main():
    print(reduce_direction(input().split(',')))


if __name__ == '__main__':
    main()
