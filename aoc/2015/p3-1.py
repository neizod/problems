#!/usr/bin/env python3


def go(point, direction):
    if direction == '^':
        return point[0]+1, point[1]
    if direction == 'v':
        return point[0]-1, point[1]
    if direction == '>':
        return point[0], point[1]+1
    if direction == '<':
        return point[0], point[1]-1


def main():
    current = (0, 0)
    visited = {current}
    for direction in input().strip():
        current = go(current, direction)
        visited |= {current}
    print(len(visited))


if __name__ == '__main__':
    main()
