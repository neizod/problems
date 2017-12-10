#!/usr/bin/env python3


try:
    while True:
        _, *ls = [int(e) for e in input().split()]
        ls = [abs(i-j) for i, j in zip(ls, ls[1:])]
        if [i+1 for i in range(len(ls))] == sorted(ls):
            print('Jolly')
        else:
            print('Not jolly')
except EOFError:
    pass
