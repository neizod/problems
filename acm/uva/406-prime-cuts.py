#!/usr/bin/env python3

N = 1000

singleton = lambda f: f()


@singleton
def primes(n=N):
    seive = [True for _ in range(n+1)]
    seive[0] = False
    seive[1] = True     # XXX WTF! an ill-desc problem that let 1 be prime!
    for idx in range(2, int(n**0.5)+1):
        if not idx:
            continue
        for change in range(2*idx, n+1, idx):
            seive[change] = False
    return [idx for idx, valid in enumerate(seive) if valid]


@singleton
def last_prime_index(n=N):
    memo = [None for _ in range(n+1)]
    index = len(primes) - 1
    while n:
        memo[n] = index
        if n == primes[index]:
            index -= 1
        n -= 1
    return memo


def solution(n, c):
    s = last_prime_index[n] + 1
    init = max(0, s//2 - c + (s%2))
    stop = min(s, s//2 + c)
    return ' '.join(str(n) for n in primes[init:stop])


def main():
    try:
        while True:
            n, c = [int(n) for n in input().split()]
            print('{} {}: {}\n'.format(n, c, (solution(n, c))))
    except EOFError:
        pass


if __name__ == '__main__':
    main()
