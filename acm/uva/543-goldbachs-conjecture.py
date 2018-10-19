#!/usr/bin/env python3

from collections import OrderedDict


def singleton(func):
    return func()


@singleton
def primes(n=10**6):
    seive = [True for _ in range(n+1)]
    seive[0] = seive[1] = False
    for idx in range(2, int(n**0.5)+1):
        if not idx:
            continue
        for change in range(2*idx, n+1, idx):
            seive[change] = False
    return OrderedDict([(idx,0) for idx, valid in enumerate(seive) if valid])


def goldbach_even(n):
    for p in primes:
        if n-p in primes:
            return p, n-p


def main():
    while True:
        n = int(input())
        if n == 0:
            break
        a, b = goldbach_even(n)
        print('{} = {} + {}'.format(n, a, b))


if __name__ == '__main__':
    main()
