chk_order = ((0,-1), (-1,0), (1,0), (0,1))

def rewalk(x, y):
    global grid, sink, chk_order, area

    if sink[y][x] != 0:
        return sink[y][x]

    diff = tuple(grid[y+chk_y][x+chk_x] for chk_x, chk_y in chk_order)
    go_x, go_y = chk_order[diff.index(min(diff))]
    if grid[y][x] > grid[y+go_y][x+go_x]:
        sink[y][x] = rewalk(x+go_x, y+go_y)
        return sink[y][x]
    else:
        area += 1
        sink[y][x] = chr(area)
        return sink[y][x]

################################################################################

for test in range(int(input())):
    size_y, size_x = [int(val) for val in input().split()]

    grid = [[10000] * (size_x+2)]
    grid += [[10000] + [int(val) for val in input().split()] + [10000] for i in range(size_y)]
    grid += [[10000] * (size_x+2)]

    sink = [[0 for i in range(size_x+2)] for i in range(size_y+2)]

    area = 96
    for y in range(1, size_y+1):
        for x in range(1, size_x+1):
            rewalk(x, y)

    print('Case #{}:'.format(test+1))
    for line in sink[1:-1]:
        print(' '.join(line[1:-1]))
