#!/usr/bin/env python3

while True:
    a, b = sorted([int(n) for n in input().split()])
    if a == -1:
        break
    print(min(b-a, 100+a-b))
