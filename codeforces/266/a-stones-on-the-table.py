#!/usr/bin/env python3

input()
stones = input().strip()
print(sum(s == t for s, t in zip(stones, stones[1:])))
