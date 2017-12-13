#!/usr/bin/env python3


def fix_corner(grid):
    for y in [0, -1]:
        for x in [0, -1]:
            grid[y][x] = True


def surround(grid, x, y):
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if (dx, dy) == (0, 0):
                continue
            if 0 <= x+dx < len(grid[0]) and 0 <= y+dy < len(grid):
                yield grid[y+dy][x+dx]


def increment(grid):
    new_grid = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for y, line in enumerate(grid):
        for x, current in enumerate(line):
            if current:
                new_grid[y][x] = sum(surround(grid, x, y)) in {2, 3}
            else:
                new_grid[y][x] = sum(surround(grid, x, y)) == 3
    fix_corner(new_grid)
    return new_grid


def main():
    steps = 100
    grid = [[c == '#' for c in input().strip()] for _ in range(100)]
    fix_corner(grid)
    for i in range(steps):
        grid = increment(grid)
    print(sum(i for line in grid for i in line))


if __name__ == '__main__':
    main()
