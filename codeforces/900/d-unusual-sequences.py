#!/usr/bin/env python3

from fractions import gcd
from operator import mul
from functools import reduce
from itertools import combinations


eval_function = lambda x: lambda f: f(x)


@eval_function(int((10**9)**0.5))
def prime(n):
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    index = 2
    for i in range(int(len(sieve)**0.5)):
        if sieve[i]:
            for j in range(2*i, len(sieve), i):
                sieve[j] = False
        index += 1
    return [i for i, is_prime in enumerate(sieve) if is_prime]


def factorized(n):
    factors = []
    for i in prime:
        if i**2 > n:
            break
        while n % i == 0:
            factors += [i]
            n //= i
    if n > 1:
        factors += [n]
    return factors


def count_coprime_parts(n, mod=None):
    count = pow(2, n-1, mod)
    unique_factors = set(factorized(n))
    for i in range(1, len(unique_factors)+1):
        for factors in combinations(unique_factors, i):
            d = reduce(mul, factors)
            count += (-1)**i * pow(2, n//d-1, mod)
            count %= mod
    return count


def solve(x, y, mod=None):
    if gcd(x, y) != x:
        return 0
    return count_coprime_parts(y//x, mod)


def main():
    x, y = [int(n) for n in input().split()]
    print(solve(x, y, 10**9+7))


if __name__ == '__main__':
    main()
