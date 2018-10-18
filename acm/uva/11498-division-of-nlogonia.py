#!/usr/bin/env python3


def coord(x, y, x0, y0):
    dx = x - x0
    dy = y - y0
    if dx == 0 or dy == 0:
        return 'divisa'
    if dx > 0 and dy > 0:
        return 'NE'
    if dx < 0 and dy > 0:
        return 'NO'
    if dx > 0 and dy < 0:
        return 'SE'
    if dx < 0 and dy < 0:
        return 'SO'


def main():
    while True:
        k = int(input())
        if not k:
            break
        x0, y0 = [int(n) for n in input().split()]
        for _ in range(k):
            x, y = [int(n) for n in input().split()]
            print(coord(x, y, x0, y0))


if __name__ == '__main__':
    main()
