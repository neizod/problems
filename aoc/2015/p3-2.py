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
    turn = 0
    santa = (0, 0)
    robot = (0, 0)
    visited = {santa, robot}
    for direction in input().strip():
        if turn == 0:
            santa = go(santa, direction)
        else:
            robot = go(robot, direction)
        visited |= {santa, robot}
        turn ^= 1
    print(len(visited))


if __name__ == '__main__':
    main()
