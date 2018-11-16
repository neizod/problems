#!/usr/bin/env python3

from collections import Counter
from functools import reduce


def diff(xs):
    return abs(xs[0] - xs[1])


def mindiff(xs, ys):
    if diff(xs) == diff(ys):
        return min([xs, ys])
    return xs if diff(xs) < diff(ys) else ys


def binsearch(books, avail):
    lo = 0
    hi = len(books) - 1
    while lo <= hi:
        mid = (lo+hi) // 2
        if books[mid] > avail:
            hi = mid - 1
        elif books[mid] < avail:
            lo = mid + 1
        else:
            return True
    return False


def decide(books, money):
    counter = Counter(books)
    output = set()
    for book in books:
        avail = money - book
        if book == avail and counter[book] == 1:
            continue
        if binsearch(books, avail):
            output |= {(book, avail)}
    return reduce(mindiff, output)


def main():
    try:
        while True:
            _ = input()
            books = sorted(map(int, input().split()))
            money = int(input())
            answer = decide(books, money)
            print('Peter should buy books whose prices are {} and {}.\n'.format(*answer))
            input()
    except EOFError:
        pass


if __name__ == '__main__':
    main()
