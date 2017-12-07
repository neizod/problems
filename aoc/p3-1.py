#!/usr/bin/env python3


def spiral_move(n):
    layer = 0
    while True:
        width = 2*layer + 1
        if n > width**2:
            layer += 1
            continue
        center = (width-2)**2 + layer
        corner = (width-2)**2 + width - 1
        while n > corner:
            n -= width - 1
        return layer + abs(n - center)


if __name__ == '__main__':
    print(spiral_move(int(input())))
