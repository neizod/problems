#!/usr/bin/env python3

from operator import mul
from functools import reduce


for test in range(int(input())):
    size = reduce(mul, [int(n) for n in input().split()])
    if size%2 == 1:
        size += 2**0.5 - 1
    print('Scenario #{}:\n{:.2f}\n'.format(test+1, size))
