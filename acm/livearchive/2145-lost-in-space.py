#!/usr/bin/env python3

from math import isclose
from itertools import permutations


class Triangle(object):
    def __init__(self, sides):
        self.sides = list(sides)

    def __repr__(self):
        return '{:.4f},{:.4f},{:.4f}'.format(*self.sides)

    @classmethod
    def from_sides(cls, sides):
        factor = 1/sides[0]
        return cls(factor*side for side in sides)

    @classmethod
    def from_points(cls, p, q, r):
        return cls.from_sides([q.distance(r), r.distance(p), p.distance(q)])

    def is_similar(self, other):
        return all(isclose(a, b, rel_tol=1e-4) for a, b in zip(self.sides, other.sides))


class Point(object):
    def __init__(self, positions):
        pos = iter(positions)
        self.x = next(pos)
        self.y = next(pos)
        self.z = next(pos)

    def distance(self, other):
        return ((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2)**0.5


def main():
    for _ in range(int(input())):
        triangle = Triangle.from_sides([float(n) for n in input().split()])
        points = [Point(float(n) for n in input().split()) for _ in range(int(input()))]
        for indexs in permutations(range(len(points)), 3):
            suspect = Triangle.from_points(*[points[i] for i in indexs])
            if triangle.is_similar(suspect):
                print(' '.join(str(i+1) for i in indexs))
                break


if __name__ == '__main__':
    main()
