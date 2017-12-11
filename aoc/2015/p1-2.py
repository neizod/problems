#!/usr/bin/env python3

from collections import Counter


floor = 0
for index, inst in enumerate(input().strip(), 1):
    if inst == '(':
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        break
print(index)
