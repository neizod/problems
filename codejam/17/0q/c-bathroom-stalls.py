#!/usr/bin/env python3

from collections import defaultdict


def is_odd(number):
    return number % 2 == 1


def calc_lr(number):
    half = number // 2
    if is_odd(number):
        return half, half
    else:
        return half-1, half


def find_stalls(stalls, persons):
    avail = defaultdict(int, {stalls: 1})
    while persons:
        choose = max(avail)
        size = avail[choose]
        del avail[choose]
        left, right = calc_lr(choose)
        if persons <= size:
            return right, left
        persons -= size
        avail[left] += size
        avail[right] += size


def main():
    for case in range(int(input())):
        n, k = [int(n) for n in input().split()]
        print('Case #{}: {} {}'.format(case+1, *find_stalls(n, k)))


if __name__ == '__main__':
    main()
