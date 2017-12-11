#!/usr/bin/env python3


def switch(grid, inst, start, stop):
    for y in range(start[1], stop[1]+1):
        for x in range(start[0], stop[0]+1):
            if inst == 'on':
                grid[y][x] += 1
            if inst == 'off':
                grid[y][x] -= 1
                grid[y][x] = max(grid[y][x], 0)
            if inst == 'toggle':
                grid[y][x] += 2
    return grid


def count(grid):
    return sum(light for line in grid for light in line)


def main():
    try:
        grid = [[0 for _ in range(1000)] for _ in range(1000)]
        while True:
            inst, start, _, stop = input().strip().replace('turn ','').split()
            start = [int(n) for n in start.split(',')]
            stop = [int(n) for n in stop.split(',')]
            grid = switch(grid, inst, start, stop)
    except EOFError:
        print(count(grid))


if __name__ == '__main__':
    main()
