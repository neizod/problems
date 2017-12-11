#!/usr/bin/env python3


try:
    total = 0
    while True:
        length = [int(n) for n in input().split('x')]
        areas = sorted(a*b for a, b in zip(length, length[1:]+length[:1]))
        total += areas[0] + 2*sum(areas)
except EOFError:
    print(total)
