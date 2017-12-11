#!/usr/bin/env python3

grid = [[1]]


def iter_ring(size):
    x = size - 1
    y = size - 2
    while y > 0:
        yield x, y
        y -= 1
    while x > 0:
        yield x, y
        x -= 1
    while y < size - 1:
        yield x, y
        y += 1
    while x < size - 1:
        yield x, y
        x += 1
    yield x, y


def iter_surround(x, y, size):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if (dx, dy) == (0, 0):
                continue
            if 0 <= x+dx < size and 0 <= y+dy < size:
                yield grid[y+dy][x+dx]


def expand(grid):
    for line in grid:
        line[:0] = ['?']
        line[len(line):] = ['?']
    size = len(line)
    grid[:0] = [['?' for _ in range(size)]]
    grid[len(grid):] = [['?' for _ in range(size)]]
    size = len(grid)
    for x, y in iter_ring(size):
        grid[y][x] = sum(v for v in iter_surround(x, y, size) if v is not '?')
        yield grid[y][x]


def find_larger(n):
    while True:
        for m in expand(grid):
            if m > n:
                return m


if __name__ == '__main__':
    print(find_larger(int(input())))
    for line in grid:
        print(' '.join('{:>6}'.format(x) for x in line))
