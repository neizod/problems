import math

class point:
    '''point class that contain position of x, y, z'''
    x = 0
    y = 0
    z = 0

def norm(p, q):
    '''actually, this is Euclidean distance, but norm is much shorter name'''
    return math.sqrt((p.x - q.x)**2 + (p.y - q.y)**2 + (p.z - q.z)**2)

def mid(a, b, c):
    '''return mid value of 3 argument'''
    return sorted([a, b, c])[1]

def normalized(a, b, c):
    '''retun 3 values which each are exactly, lesser than and greater than 1'''
    d = mid(a, b, c)
    return a/d, b/d, c/d

def match(ijk, pqr):
    '''check if triangle ijk match pqr, return matched point order on success'''
    so = sorted(ijk)
    sc = sorted(pqr)
    err = 0.00001
    ## check triangle matched ##
    if so[0]-err <= sc[0] <= so[0]+err and so[2]-err <= sc[2] <= so[2]+err:
        ## check point matching ##
        if pqr[0]-err <= ijk[0] <= pqr[0]+err:
            if pqr[1]-err <= ijk[1] <= pqr[1]+err:
                return 'ijk'
            else:
                return 'ikj'
        elif pqr[1]-err <= ijk[0] <= pqr[1]+err:
            if pqr[2]-err <= ijk[1] <= pqr[2]+err:
                return 'kij'
            else:
                return 'jik'
        else:
            if pqr[0]-err <= ijk[1] <= pqr[0]+err:
                return 'jki'
            else:
                return 'kji'
    return False

################################################################################

import re

raw = input()
for no_i in range(int(raw)):
    raw = input()
    raw = re.split(' +', raw)
    qr = float(raw[0])
    rp = float(raw[1])
    pq = float(raw[2])
    pqr = normalized(qr, rp, pq)

    ## create list of points name lpoint ##
    raw = input()
    npoint = int(raw)
    lpoint = [point() for m in range(npoint)]
    for i in range(npoint):
        raw = input()
        raw = re.split(' +', raw)
        lpoint[i].x = float(raw[0])
        lpoint[i].y = float(raw[1])
        lpoint[i].z = float(raw[2])

    ## loop through all set of 3 points ##
    for i in range(npoint-2):
        for j in range(i+1, npoint-1):
            for k in range(j+1, npoint):
                jk = norm(lpoint[j], lpoint[k])
                ki = norm(lpoint[k], lpoint[i])
                ij = norm(lpoint[i], lpoint[j])
                ijk = normalized(jk, ki, ij)

                ## try get and order of matching ##
                order = match(ijk, pqr)
                if order:
                    for c in order:
                        if c == 'i':
                            print(i+1, end='')
                        elif c == 'j':
                            print(j+1, end='')
                        else:
                            print(k+1, end='')
                        print(end=' ')
                    print('')
