def show(triangle, center=True):
    '''print a readable triangle, for fast debugging purpose'''
    for line in triangle:
        if center:
            print(' '*(n-(len(line)+1)//2), end='')
        for each in line:
            print(each, end='')
        print('')

def retri_dn(i, j, s=1):
    '''recursive function finding bigger triangle downward'''
    if i+s <= n-j//2-1:
        chk = True
        if triangle[i+s][j] == 1:
            for a in range(s):
                for b in range(2):
                    if triangle[i+a][j+2*(s-1-a)+(b+1)] == 0:
                        chk = False
        else:
            return s
        if chk:
            return retri_dn(i, j, s+1)
    return s

def retri_up(i, j, s=1):
    '''recursive function finding bigger triangle upward'''
    if i-s >= 0 and j+2*s <= 2*(n-i-1):
        chk = True
        if triangle[i-s][j+2*s] == 1:
            for a in range(s):
                for b in range(2):
                    if triangle[i-a][j+2*s-b] == 0:
                        chk = False
        else:
            return s
        if chk:
            return retri_up(i, j, s+1)
    return s

################################################################################

scene = 0
while True:
    scene += 1
    raw = input()
    n = int(raw)
    if n == 0:
        break

    ## create triangle in form of list, the 1st index of each row always be 0 ##
    triangle = [[] for i in range(n)]
    for i in range(n):
        raw = input()
        for j in range(i, 2*n-i-1):
            if raw[j] == '#':
                triangle[i].append(0)
            else:
                triangle[i].append(1)
    ## uncomment below to see the triangle ##
    # show(triangle)

    ## create list of biggest size of each small triangle ##
    bigtri = []
    ## loop through all small triangle ##
    for i in range(n):
        for j in range(0, 2*(n-i)-1):
            ## and make sure to use upward or downward checking ##
            if j%2 == 0:
                if triangle[i][j] == 1:
                    bigtri.append(retri_dn(i, j))
            else:
                if triangle[i][j] == 1:
                    bigtri.append(retri_up(i, j))
 
    print('Triangle #{}'.format(scene))
    print('The largest triangle area is {}.'.format(max(bigtri)**2))
    print('')
