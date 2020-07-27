#!/usr/bin/env python3

from collections import Counter


def fusable(shards):
    c = Counter(shards)
    if abs(c['A'] - c['B']) == 1:
        return True
    return False


def main():
    for c in range(int(input())):
        input()
        shards = input().strip()
        print(f'Case #{c+1}: {"NY"[fusable(shards)]}')


if __name__ == '__main__':
    main()
