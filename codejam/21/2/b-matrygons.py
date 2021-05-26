#!/usr/bin/env python3

from types import SimpleNamespace as namespace
from operator import mul
from functools import reduce
from itertools import product
from collections import Counter


def iter_primes(memo=namespace(pi=0, ps=[2, 3])):
    k = 0
    while True:
        while len(memo.ps) <= k:
            head = memo.ps[memo.pi]**2 + 1
            memo.pi += 1
            tail = memo.ps[memo.pi]**2
            seive = list(range(head, tail))
            for p in memo.ps[:memo.pi]:
                size = 1 + (tail - head + (head % -p)) // p
                seive[-head%p::p] = [0] * size
            memo.ps += (p for p in seive if p)
        yield memo.ps[k]
        k += 1


def factors(n):
    if n == 1:
        yield 1
        return
    for p in iter_primes():
        if p**2 > n:
            break
        while n % p == 0:
            yield p
            n //= p
    if n > 1:
        yield n


def divisors(n):
    gfs = ({p**i for i in range(k+1)} for p, k in Counter(factors(n)).items())
    yield from (reduce(mul, ts) for ts in product(*gfs))


def aux(n, memo=[(), ()]):
    while len(memo) < n+1:
        candidates = [(d, *memo[len(memo)//d-1]) for d in divisors(len(memo)) if d > 1]
        if not candidates:
            memo += [(len(memo),)]
        else:
            memo += [max(candidates, key=len)]
    return memo[n]


def matrygon(n):
    return max(((d, *aux(n//d-1)) for d in divisors(n) if d >= 3), key=len)


def main():
    for case in range(int(input())):
        n = int(input())
        answer = matrygon(n)
        print(f'Case #{case+1}: {len(answer)}')


if __name__ == '__main__':
    main()
