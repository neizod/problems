#!/usr/bin/env python3

def divisible(ls):
    for i, a in enumerate(ls):
        for b in ls[i+1:]:
            if a % b == 0 or b % a == 0:
                yield sorted([a, b])

try:
    checksum = 0
    while True:
        numbers = [int(n) for n in input().split()]
        x, y = next(divisible(numbers))
        checksum += y // x
except EOFError:
    print(checksum)
