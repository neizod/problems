def show(map):
    '''print a readable map, for fast debugging purpose'''
    for line in map:
        print(line)

def refill(x, y):
    '''recursive fill in like paint program, change 0 to 4'''
    if not 0 < x <= width or not 0 < y <= height:
        return
    if fmap[y][x] == 0:
        fmap[y][x] = 4
        refill(x+1, y)
        refill(x, y+1)
        refill(x-1, y)
        refill(x, y-1)

def rechk_mv(xbox, ybox, xman, yman, move=0):
    '''recursive move box around map'''
    global omap, fmap, finalmove
    if xbox == xfin and ybox == yfin:
        ## check if the box already in goal, this can be many approaches ##
        finalmove.append(move)

    ## clone original-map to fill-map for refill() ##
    fmap = [omap[i][:] for i in range(height+2)]
    fmap[ybox][xbox], fmap[yman][xman] = 1, 0
    refill(xman, yman)
    compass = chk_bx(xbox, ybox)

    ## to see the recursive flow, enable the next line ##
    # print('box', xbox, ybox, ' man', xman, yman, ' ', compass, move)
    if chk_hs(xbox, ybox, compass, move):
        move += 1
        if compass[0] == 'N':
            rechk_mv(xbox, ybox-1, xbox, ybox, move)
        if compass[1] == 'E':
            rechk_mv(xbox+1, ybox, xbox, ybox, move)
        if compass[2] == 'W':
            rechk_mv(xbox-1, ybox, xbox, ybox, move)
        if compass[3] == 'S':
            rechk_mv(xbox, ybox+1, xbox, ybox, move)

def chk_bx(x, y):
    '''check if that the man can move the box, return in compass direction'''
    compass = '    '
    if fmap[y+1][x] == 4 and (fmap[y-1][x] == 0 or fmap[y-1][x] == 4):
        compass = 'N' + compass[1:4]
    if fmap[y][x-1] == 4 and (fmap[y][x+1] == 0 or fmap[y][x+1] == 4):
        compass = compass[0:1] + 'E' + compass[2:4]
    if fmap[y][x+1] == 4 and (fmap[y][x-1] == 0 or fmap[y][x-1] == 4):
        compass = compass[0:2] + 'W' + compass[3:4]
    if fmap[y-1][x] == 4 and (fmap[y+1][x] == 0 or fmap[y+1][x] == 4):
        compass = compass[0:3] + 'S'
    return compass

def chk_hs(x, y, compass, move):
    '''check history-map if the box has been visited, return true if not'''
    for i in range(len(hmap[y][x])):
        if compass == hmap[y][x][i]:
            if move >= nmap[y][x][i]:
                return False
            else:
                nmap[y][x][i] = move
                return True
    hmap[y][x].append(compass)
    nmap[y][x].append(move)
    return True

def result():
    '''handle the many approaches and no-approach'''
    if finalmove != []:
        return min(finalmove)
    else:
        return -1

################################################################################

import re

while True:
    raw = input()
    raw = re.split(' +', raw)
    width, height = int(raw[0]), int(raw[1])
    if width == 0 and height == 0:
        break

    ## create original-map: the man, the goal, and the box are not include ##
    ## the map also wrap with 1 to prevent the out-of-bound problems ##
    omap = []
    omap.append([1 for n in range(width+2)])
    for i in range(height):
        raw = input()
        raw = re.split(' +', raw)
        for j in range(width):
            raw[j] = int(raw[j])
            ## kept only position of each and remove them ##
            if raw[j] == 4:    # the man
                xman, yman = j+1, i+1
                raw[j] = 0
            if raw[j] == 3:    # the goal
                xfin, yfin = j+1, i+1
                raw[j] = 0
            if raw[j] == 2:    # the box
                xbox, ybox = j+1, i+1
                raw[j] = 0
        omap.append([1] + [raw[n] for n in range(width)] + [1])
    omap.append([1 for n in range(width+2)])

    ## also create history-map to check visited, and n-map for move number ##
    hmap = [[[] for i in range(width+2)] for j in range(height+2)]
    nmap = [[[] for i in range(width+2)] for j in range(height+2)]
    finalmove = []

    ## main routine start here! (its recursive!!!) ##
    rechk_mv(xbox, ybox, xman, yman)
    print(result())
