#!/usr/bin/env python3

bin2base = lambda num, base: int(bin(num)[2:], base)


def small_proper_factor(num):
    for prime in [2, 3, 5, 7]:
        if num % prime == 0:
            return prime
    raise ValueError


def all_bases(val):
    return [small_proper_factor(bin2base(val, b)) for b in range(2, 11)]


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
