#!/usr/bin/env python3


def ceil_div(n, k):
    return n//k + (n%k!=0)


def lowbit(x):
    return x & (-x)


def sum_until(rs, n):
    c = 0
    while n > 0:
        c += rs[n]
        n -= lowbit(n)
    return c


def increase(rs, n):
    while n < len(rs):
        rs[n] += 1
        n += lowbit(n)


def method_a(ls, k):
    ls = [1+(n-1)//k for n in ls]
    rs = [0 for _ in range(1+ceil_div(len(ls), k))]
    c = 0
    for i, n in enumerate(ls):
        c += i - sum_until(rs, n)
        increase(rs, n)
    return c


def method_b(ls, k):
    ls = [(n-1)//k for n in ls]
    def aux(i, go_zone):
        at_zone = i // k
        if go_zone < at_zone:
            return (go_zone+1)*k - 1 - i
        if go_zone > at_zone:
            return go_zone*k - i
        return 0
    return max(abs(aux(i, go_zone)) for i, go_zone in enumerate(ls))


if __name__ == '__main__':
    for t in range(int(input())):
        _, k = [int(n) for n in input().split()]
        ns = [int(n) for n in input().split()]
        print('Case {}: {}'.format(t+1, method_a(ns, k)-method_b(ns, k)))
