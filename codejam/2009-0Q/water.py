from collections import namedtuple
point = namedtuple('point', 'x, y')

def smallest_neig(x, y, grid, size):
    dest = point(x, y)
    smallest = grid[y][x]
    for chk in [point(0, -1), point(-1, 0), point(1, 0), point(0, 1)]:
        go = point(x + chk.x, y + chk.y)
        if 0 <= go.x < size.x and 0 <= go.y < size.y:
            value = grid[go.y][go.x] 
            if value < smallest:
                smallest = value
                dest = go
    return dest

def rewalk(x, y, grid, sink, size, area):
    if sink[y][x]:
        return sink[y][x]

    dest = smallest_neig(x, y, grid, size)
    if grid[y][x] > grid[dest.y][dest.x]:
        sink[y][x] = rewalk(dest.x, dest.y, grid, sink, size, area)
    else:
        sink[y][x] = area.pop(0)
    return sink[y][x]

def sink_it(grid, size):
    sink = [[None for i in range(size.x)] for i in range(size.y)]
    area = [chr(97+i) for i in range(26)]
    for y in range(size.y):
        for x in range(size.x):
            rewalk(x, y, grid, sink, size, area)
    return sink

def test(case):
    size = point(*[int(n) for n in input().split()][::-1])
    grid = [[int(n) for n in input().split()] for i in range(size.y)]
    return sink_it(grid, size)

def main():
    for case in range(int(input())):
        output = test(case)
        print('Case #{}:'.format(case+1))
        for line in output:
            print(' '.join(line))

if __name__ == '__main__':
    main()

