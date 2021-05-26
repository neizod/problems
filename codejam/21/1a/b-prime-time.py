#!/usr/bin/env python3

from copy import deepcopy


def refind(primes, product=1, i=0):
    summation = sum(k*p for p, k in primes)
    if summation == product:
        return product
    if summation < product:
        return 0
    point = 0
    for j in range(i, len(primes)):
        if primes[j][1] == 0:
            continue
        alter_primes = deepcopy(primes)
        alter_primes[j][1] -= 1
        alter_product = product * primes[j][0]
        point = max(point, refind(alter_primes, alter_product, j))
    return point


def main():
    for case in range(int(input())):
        primes = [[int(x) for x in input().split()] for _ in range(int(input()))]
        answer = refind(primes)
        print(f'Case #{case+1}: {answer}')


if __name__ == '__main__':
    main()
