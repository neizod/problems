#!/usr/bin/env python3

try:
    count_valid = 0
    while True:
        words = input().split()
        if len(words) == len(set(words)):
            count_valid += 1
except EOFError:
    print(count_valid)
