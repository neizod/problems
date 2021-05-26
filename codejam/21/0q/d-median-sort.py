#!/usr/bin/env python3


def ask(a, b, c):
    print(a, b, c)
    return int(input())


def answer(xs):
    print(*xs)
    return int(input()) == 1


def find_lo_hi(x, left=None, right=None):
    if left is None or right is None:
        return -1, x-1
    q, r = divmod(right-left, 3)
    dl, dr = q+bool(r), q
    if right-left == 2 and right == x-1:
        dl, dr = dr, dl
    return left+dl, right-dr


def interact_median_sort(n):
    xs = [1, 2, 3]
    mid = ask(*xs)
    xs.remove(mid)
    xs[1:1] = [mid]
    for x in range(4, n+1):
        left, right = find_lo_hi(x)
        while right-left > 1:
            lo, hi = find_lo_hi(x, left, right)
            mid = ask(xs[lo], xs[hi], x)
            if mid == xs[lo]:
                right = lo
            elif mid == xs[hi]:
                left = hi
            else:
                left = lo
                right = hi
        xs[right:right] = [x]
    return answer(xs)


def main():
    cases, n, _ = [int(x) for x in input().split()]
    for case in range(cases):
        if not interact_median_sort(n):
            break


if __name__ == '__main__':
    main()
