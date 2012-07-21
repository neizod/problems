# acm thailand 2011

def refill(lf_c, lf_h, lf_v, path=''):
    '''recursive fill the walk path, if filled check if the walk are valid'''
    global answer
    if answer:
        return
    if lf_c == 0 and lf_h == 0 and lf_v == 0:
        if chk(path):
            ## on valid path, ignore furthermore path ##
            answer = True
            print(len(path))
        return
    ## must start from left_center to make sure the shortest path come first ##
    if lf_c > 0:
        refill(lf_c-1, lf_h, lf_v, path + 'c')
    if lf_h > 0:
        refill(lf_c, lf_h-1, lf_v, path + 'h')
    if lf_v > 0:
        refill(lf_c, lf_h, lf_v-1, path + 'v')

def walk(n):
    '''loop through all possible walk path pattern'''
    for i in range(n+1):
        refill(n-i, i, i)

def chk(path):
    '''check if the walk path is valid by test walk with xmap'''
    x, y = 0, 0
    for ew in path:
        if xmap[y][x] != '':
            for ec in xmap[y][x]:
                if ec == ew:
                    return False
        if ew == 'c':
            x += 1
            y += 1
        if ew == 'h':
            x += 1
        if ew == 'v':
            y += 1
    return True

################################################################################

while True:
    size = int(input())
    if size == 0:
        break

    ## create xmap - the map of invalid step ##
    xmap = [['' for j in range(size+1)] for i in range(size+1)]
    for j in range(size):
        inrow = input()
        for i in range(size):
            if inrow[i] == '#':
                xmap[j][i] += 'c'
                if j > 0:
                    if xmap[j-1][i] != '':
                        xmap[j][i] += 'h'
                if i > 0:
                    if xmap[j][i-1] != '':
                        xmap[j][i] += 'v'

    ## for fast execution, loop through shortest first and stop if answered ##
    answer = False
    walk(size)
