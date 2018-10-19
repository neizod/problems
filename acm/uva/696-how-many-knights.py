#!/usr/bin/env python3


def knight(n, m):
    if min(n, m) == 1:
        return max(n, m)
    if min(n, m) == 2:
        p, q = divmod(max(n, m), 4)
        return 4*p + 2*min(q, 2)
    return (n*m+1)//2


def main():
    while True:
        n, m = [int(i) for i in input().split()]
        if n == m == 0:
            break
        ans = knight(n, m)
        print('{} knights may be placed on a {} row {} column board.'.format(ans, n, m))


if __name__ == '__main__':
    main()
