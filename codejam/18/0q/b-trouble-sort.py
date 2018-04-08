#!/usr/bin/env python3

from itertools import count


def trouble_sort(ls):
    ls[0::2] = sorted(ls[0::2])
    ls[1::2] = sorted(ls[1::2])
    return ls


def check_trouble_sort(ls):
    ls = trouble_sort(ls)
    it = iter(ls); next(it)
    for index, a, b in zip(count(), ls, it):
        if a > b:
            return index
    return -1


def main():
    for case in range(int(input())):
        input()
        ls = [int(n) for n in input().split()]
        answer = check_trouble_sort(ls)
        if answer == -1:
            answer = 'OK'
        print('Case #{}: {}'.format(case+1, answer))


if __name__ == '__main__':
    main()
