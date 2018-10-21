#!/usr/bin/env python3

from collections import Counter


singleton = lambda f: f()


@singleton
def primes(n=10**5):
    seive = [True for _ in range(n+1)]
    seive[0] = seive[1] = False
    for idx in range(2, int(n**0.5)+1):
        if not idx:
            continue
        for change in range(2*idx, n+1, idx):
            seive[change] = False
    return [idx for idx, valid in enumerate(seive) if valid]


def factorized(n):
    for p in primes:
        if p**2 > n:
            break
        while n % p == 0:
            n //= p
            yield p
    if n > 1:
        yield n


def reducing(ls):
    freq = Counter(ls)
    while freq[3] >= 2:
        freq[3] -= 2
        freq[9] += 1
    while freq[2] >= 3:
        freq[2] -= 3
        freq[8] += 1
    while freq[2] >= 1 and freq[3] >= 1:
        freq[2] -= 1
        freq[3] -= 1
        freq[6] += 1
    while freq[2] >= 2:
        freq[2] -= 2
        freq[4] += 1
    return freq


def prod_digit(n):
    ls = list(factorized(n)) or [n]
    if any(m > 9 for m in ls):
        return None
    return ''.join(k*str(p) for p, k in sorted(reducing(ls).items()))


def main():
    for _ in range(int(input())):
        n = prod_digit(int(input()))
        print(n if n is not None else -1)


if __name__ == '__main__':
    main()
