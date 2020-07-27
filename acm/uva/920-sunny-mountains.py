#!/usr/bin/env python3

from collections import namedtuple


Point = namedtuple('Point', 'x y')
Point.from_str = lambda s: Point(*map(int, s.split()))


def find_length(p, q):
    return ( (p.x - q.x)**2 + (p.y - q.y)**2 )**0.5


def proportion_length(p, q, r):
    return find_length(p, q) * (p.y - r.y) / (p.y - q.y)


def beautiful_sunny_length(points):
    length = 0
    best = Point(x=None, y=0)
    points.sort(reverse=True)
    for prev, curr in zip(points, points[1:]):
        if curr.y > best.y:
            length += proportion_length(curr, prev, best)
            best = curr
    return length


def main():
    for _ in range(int(input())):
        points = [Point.from_str(input()) for _ in range(int(input()))]
        answer = beautiful_sunny_length(points)
        print('{:.2f}'.format(answer))


if __name__ == '__main__':
    main()
