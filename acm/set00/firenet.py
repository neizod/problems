def replace(x, y, imap, d=0):
    '''recursive place a gun house'''
    global size, finalplace
    if imap[y][x] >= 1:
        finalplace.append(d)
        return

    ## create a fill-map and mark unplacable point ##
    fmap = [imap[i][:] for i in range(size+2)]
    fmap = mark(x, y, fmap)

    ## recursive here through all ramaning (x, y) in the map ##
    for j in range(1, size+1):
        if j < y:
            continue
        for i in range(1, size+1):
            if j == y and i < x:
                continue
            replace(i, j, fmap, d+1)

def mark(x, y, amap):
    '''maek unplacable (x, y)'''
    amap[y][x] = 2
    i = 1    # north
    while amap[y][x-i] != 1:
        amap[y][x-i] = 2
        i += 1
    i = 1    # east
    while amap[y+i][x] != 1:
        amap[y+i][x] = 2
        i += 1
    i = 1    # west
    while amap[y-i][x] != 1:
        amap[y-i][x] = 2
        i += 1
    i = 1    # south
    while amap[y][x+i] != 1:
        amap[y][x+i] = 2
        i += 1
    return amap

################################################################################

while True:
    raw = input()
    size = int(raw)
    if size == 0:
        break

    ## create original-map, wrap map with 1 ##
    omap = []
    omap.append([1 for n in range(size+2)])
    for i in range(size):
        raw = input()
        ins = []
        for j in range(size):
            if raw[j] == '.':
                ins.append(0)
            else:
                ins.append(1)
        omap.append([1] + ins + [1])
    omap.append([1 for n in range(size+2)])

    ## recursive place-in a gun house and find how many of them ##
    finalplace = []
    for j in range(size+1):
        for i in range(size+1):
            replace(i, j, omap)
    print(max(finalplace))
