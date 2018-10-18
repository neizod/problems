#!/usr/bin/env python3

from math import exp, sin, cos, tan, isclose


def f(x, p, q, r, s, t, u):
    return p*exp(-x) + q*sin(x) + r*cos(x) + s*tan(x) + t*x**2 + u


def bisect(ns):
    lo, hi = 0, 1
    init = f(lo, *ns)
    last = f(hi, *ns)
    if init * last > 0:
        return None
    while True:
        mid = (lo+hi) / 2
        ans = f(mid, *ns)
        if isclose(ans, 0, abs_tol=1e-9):
            return mid
        elif ans > 0:
            lo = mid
        elif ans < 0:
            hi = mid


def main():
    try:
        while True:
            ns = [int(i) for i in input().split()]
            answer = bisect(ns)
            if answer is None:
                print('No solution')
            else:
                print('{:.4f}'.format(answer))
    except EOFError:
        pass


if __name__ == '__main__':
    main()
