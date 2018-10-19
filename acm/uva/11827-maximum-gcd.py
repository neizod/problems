#!/usr/bin/env python3

from fractions import gcd
from itertools import combinations


def main():
    for _ in range(int(input())):
        ls = [int(n) for n in input().split()]
        print(max(gcd(a, b) for a, b in combinations(ls, 2)))


if __name__ == '__main__':
    main()
