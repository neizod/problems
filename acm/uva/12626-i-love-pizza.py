#!/usr/bin/env python3

from collections import Counter


def main():
    require = Counter('MARGARITA')
    for _ in range(int(input())):
        available = Counter(input())
        print(min(available[key] // value for key, value in require.items()))


if __name__ == '__main__':
    main()
