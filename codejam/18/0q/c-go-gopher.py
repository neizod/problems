#!/usr/bin/env python3

import sys


def interact(size):
    x = 42
    y = 23
    holes_dug = set()
    while True:
        print(x, y)
        rx, ry = [int(n) for n in input().split()]
        if rx == ry == -1:
            sys.exit(42)
        elif rx == ry == 0:
            break
        holes_dug |= {(rx, ry)}
        if len(holes_dug) == 9:
            holes_dug.clear()
            y += 3


def main():
    for case in range(int(input())):
        size = int(input())
        interact(size)


if __name__ == '__main__':
    main()
