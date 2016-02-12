#!/usr/bin/env python3


def make_seq(n):
    os = list(range(1, n, 2))
    es = list(range(2, n, 2))
    ls = os[:]
    if n % 2 != 0:
        ls += [n]
    ls += os[::-1]
    ls += [n]
    ls += es
    if n % 2 == 0:
        ls += [n]
    ls += es[::-1]
    return ls


def main():
    print(' '.join(str(n) for n in make_seq(int(input()))))


if __name__ == '__main__':
    main()
