#!/usr/bin/env python3

from math import isclose


def aux(c, journey):
    return sum(d/(s+c) for d, s in journey)


def bound(t, journey):
    step = 1e-09
    lower = upper = -min(s for _, s in journey) + step
    while True:
        upper += step
        if aux(upper, journey) < t:
            break
        step *= 2
    return lower, upper


def bisect(t, journey):
    lower, upper = bound(t, journey)
    for _ in range(2000):
        c = (lower + upper) / 2
        x = aux(c, journey)
        if isclose(x, t):
            break
        elif x > t:
            lower = c
        else:
            upper = c
    return c


def main():
    r, t = [int(n) for n in input().split()]
    journey = [tuple(int(n) for n in input().split()) for _ in range(r)]
    print(bisect(t, journey))


if __name__ == '__main__':
    main()
