#!/usr/bin/env python3

from math import isclose


def parse(string):
    ns = [int(n) for n in string.split() if n.isdigit()]
    if 'Fuel' in string:
        return ns[0], ns[1]
    if 'Leak' in string:
        return ns[0], 'L'
    if 'Gas' in string:
        return ns[0], 'S'
    if 'Mechanic' in string:
        return ns[0], 'M'
    if 'Goal' in string:
        return ns[0], 'G'


def journey(size, ls):
    it = iter(ls)
    prev, rate = next(it)
    rate /= 100
    leak = 0
    tank = size
    for curr, event in it:
        dist = curr - prev
        prev = curr
        tank -= dist * (rate + leak)
        if tank < 0:
            return False
        if event == 'L':
            leak += 1
        elif event == 'S':
            tank = size
        elif event == 'M':
            leak = 0
        elif event == 'G':
            return tank >= 0
        else:
            rate = event / 100


def init_bisect(ls):
    lo, hi = 0, 1
    while not journey(hi, ls):
        lo = hi
        hi *= 2
    return lo, hi


def bisect_journey(ls):
    lo, hi = init_bisect(ls)
    while not isclose(lo, hi):
        mid = (lo + hi) / 2
        if journey(mid, ls):
            hi = mid
        else:
            lo = mid
    return lo


def main():
    while True:
        curr, event = parse(input())
        if event == 0:
            break
        ls = [(curr, event)]
        while True:
            curr, event = parse(input())
            ls += [(curr, event)]
            if event == 'G':
                break
        print('{:.3f}'.format(bisect_journey(ls)))


if __name__ == '__main__':
    main()
