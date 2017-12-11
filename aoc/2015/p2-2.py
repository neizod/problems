#!/usr/bin/env python3

from operator import mul
from functools import reduce


try:
    total = 0
    while True:
        length = [int(n) for n in input().split('x')]
        total += reduce(mul, length) + 2*sum(sorted(length)[:2])
except EOFError:
    print(total)
