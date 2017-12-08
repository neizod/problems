#!/usr/bin/env python3

import mathapi      # //github.com/neizod/mathapi

bin2base = lambda num, base: int(bin(num)[2:], base)


def real_factor(num):
    factors = mathapi.factorized(num)
    if len(factors) == 1:
        raise ValueError
    return factors[0]


def all_bases(val):
    return [real_factor(bin2base(val, b)) for b in range(2, 11)]


def find_valid_coins(n, j):
    val = (1 << n-1) + 1
    while j:
        try:
            factors = all_bases(val)
        except ValueError:
            pass
        else:
            j -= 1
            print(bin(val)[2:], *factors)
        val += 2


def main():
    for case in range(int(input())):
        print('Case #{}:'.format(case+1))
        n, j = [int(i) for i in input().split()]
        find_valid_coins(n, j)


if __name__ == '__main__':
    main()
