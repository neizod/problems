#!/usr/bin/env python3


def knight(n, m):
    return (n*m+1)//2


def rook(n, m):
    return min(n, m)


def queen(n, m):
    return min(n, m)


def king(n, m):
    return ((n+1)//2) * ((m+1)//2)


def maxmove(t, n, m):
    return {'K': king, 'Q': queen, 'k': knight, 'r': rook}[t](n, m)


def main():
    for _ in range(int(input())):
        t, raw = input().split(maxsplit=1)
        n, m = [int(i) for i in raw.split()]
        print(maxmove(t, n, m))


if __name__ == '__main__':
    main()
