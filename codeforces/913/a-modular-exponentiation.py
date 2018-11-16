#!/usr/bin/env python3


def revpowmod(n, m):
    if n > 30:
        return m
    return m % (2**n)


def main():
    n = int(input())
    m = int(input())
    print(revpowmod(n, m))


if __name__ == '__main__':
    main()
