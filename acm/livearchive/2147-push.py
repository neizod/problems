#!/usr/bin/env python3

from enum import IntEnum
from copy import deepcopy


class Notation(IntEnum):
    FLOOR = 0
    WALL = 1
    BOX = 2
    GOAL = 3
    MAN = 4


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def shift(self, dx, dy):
        return type(self)(self.x+dx, self.y+dy)


class Grid(object):
    DIRECTIONS = [ (0, -1, 'N'),
                   (+1, 0, 'E'),
                   (-1, 0, 'W'),
                   (0, +1, 'S') ]

    def __init__(self, grid):
        self.grid = grid
        self.height = len(grid)
        self.width = len(next(iter(grid)))

    def __getitem__(self, point):
        return self.grid[point.y][point.x]

    def __setitem__(self, point, value):
        self.grid[point.y][point.x] = value

    def has_coord(self, point):
        return 0 <= point.x < self.width and 0 <= point.y < self.height


class Puzzle(object):
    def __init__(self, layout, goal):
        self.goal = goal
        self.layout = Grid(layout)
        self.history = None

    def walk(self, man, reachable):
        if reachable.has_coord(man):
            if reachable[man] == Notation.FLOOR:
                reachable[man] = Notation.MAN
                for dx, dy, _ in Grid.DIRECTIONS:
                    self.walk(man.shift(dx, dy), reachable)

    def pushable_directions(self, box, reachable):
        compass = ''
        for dx, dy, name in Grid.DIRECTIONS:
            before = box.shift(-dx, -dy)
            after = box.shift(dx, dy)
            if ( reachable.has_coord(before) and reachable.has_coord(after)
                 and reachable[before] == Notation.MAN
                 and self.layout[after] == Notation.FLOOR ):
                compass += name
            else:
                compass += ' '
        return compass

    def push(self, box, man, move=0):
        if box == self.goal:
            return [move]
        reachable = deepcopy(self.layout)
        reachable[box] = Notation.WALL
        self.walk(man, reachable)
        compass = self.pushable_directions(box, reachable)
        answers = []
        if not self.is_visited(box, compass, move):
            for dx, dy, name in Grid.DIRECTIONS:
                if name in compass:
                    answers += self.push(box.shift(dx, dy), box, move+1)
        return answers

    def is_visited(self, box, compass, move):
        if compass not in self.history[box] or move < self.history[box][compass]:
            self.history[box][compass] = move
            return False
        return True

    def solve(self, box, man):
        self.history = Grid([ [{} for _ in range(self.layout.width)]
                                  for _ in range(self.layout.height) ])
        answers = self.push(box, man)
        return min(answers) if answers else -1


def extract_information(grid):
    info = [None for _ in range(3)]
    for y, line in enumerate(grid):
        for x, value in enumerate(line):
            if value >= 2:
                info[value-2] = Point(x, y)
                grid[y][x] = 0
    return (grid, *info)


def main():
    while True:
        width, height = [int(n) for n in input().split()]
        if (width, height) == (0, 0):
            break
        grid = [[int(n) for n in input().split()] for _ in range(height)]
        grid, box, goal, man = extract_information(grid)
        print(Puzzle(grid, goal).solve(box, man))


if __name__ == '__main__':
    main()
