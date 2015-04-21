#!/usr/bin/env python3

def find_gaps(mushrooms):
    return [max(mi-mj, 0) for mi, mj in zip(mushrooms, mushrooms[1:])]


def vary(mushrooms):
    return sum(find_gaps(mushrooms))


def const(mushrooms):
    mx = max(find_gaps(mushrooms))
    return sum(min(mx, mi) for mi in mushrooms[:-1])


for case in range(int(input())):
    input()
    mushrooms = [int(n) for n in input().split()]
    ans_vary = vary(mushrooms)
    ans_const = const(mushrooms)
    print('Case #{}: {} {}'.format(case+1, ans_vary, ans_const))
