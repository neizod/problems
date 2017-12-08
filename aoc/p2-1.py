#!/usr/bin/env python3

try:
    checksum = 0
    while True:
        numbers = [int(n) for n in input().split()]
        checksum += max(numbers) - min(numbers)
except EOFError:
    print(checksum)
