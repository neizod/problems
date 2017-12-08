#!/usr/bin/env python3

while True:
    n, _ = [int (n) for n in input().split()]
    if n == 0:
        break
    bs = [int(n) for n in input().split()]
    possible = {abs(a-b) for a in bs for b in bs}
    print('Y' if len(possible) == n+1 else 'N')
