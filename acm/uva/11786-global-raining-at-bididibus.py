#!/usr/bin/env python3


def rain(valley):
    down = []
    water = 0
    for curr, slope in enumerate(valley):
        if slope == '\\':
            down += [curr]
        if slope == '/' and down:
            prev = down.pop()
            water += curr - prev
    return water


def main():
    for _ in range(int(input())):
        valley = input().strip()
        water = rain(valley)
        print(water)


if __name__ == '__main__':
    main()
