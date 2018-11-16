#!/usr/bin/env python3

import random
from itertools import count
from collections import namedtuple


Point = namedtuple('Point', 'x y')
Point.from_spec = lambda st: Point(*[float(si) for si in st.split()])

Circle = namedtuple('Circle', 'c r')
Circle.__new__.__defaults__ = (Point(0, 0), 0)
Circle.__contains__ = lambda s, p: s.r > 0 and sq_dist(p, s.c) <= s.r**2
Circle.from_arc = lambda *ps: ( circle_from_1_points(*ps) if len(ps) == 1 else
                                circle_from_2_points(*ps) if len(ps) == 2 else
                                circle_decide_3_points(*ps) if len(ps) == 3 else
                                NotImplemented )

sq_dist = lambda p, q=Point(0, 0): (p.x-q.x)**2 + (p.y-q.y)**2

det = lambda u, v, w: u.x*v.y + v.x*w.y + w.x*u.y - u.x*w.y - v.x*u.y - w.x*v.y
detx = lambda u, v, w: ( sq_dist(u)*v.y + sq_dist(v)*w.y + sq_dist(w)*u.y
                       - sq_dist(u)*w.y - sq_dist(v)*u.y - sq_dist(w)*v.y )
dety = lambda u, v, w: ( u.x*sq_dist(v) + v.x*sq_dist(w) + w.x*sq_dist(u)
                       - u.x*sq_dist(w) - v.x*sq_dist(u) - w.x*sq_dist(v) )
dets = lambda u, v, w: ( u.x*v.y*sq_dist(w) + v.x*w.y*sq_dist(u) + w.x*u.y*sq_dist(v)
                       - u.x*w.y*sq_dist(v) - v.x*u.y*sq_dist(w) - w.x*v.y*sq_dist(u) )


def shuffled(points):
    ls = list(points)
    random.shuffle(ls)
    return ls


# XXX please note that though the problem statement says 2 <= n <= 100,
#     the actual test does contain case of n == 1 too. WTF!!!
def circle_from_1_points(p1):
    return Circle(p1, 0)


def circle_from_2_points(p1, p2):
    dx = (p1.x + p2.x)/2
    dy = (p1.y + p2.y)/2
    c = Point(dx, dy)
    r = sq_dist(p1, p2)**.5/2
    return Circle(c, r)


def circle_from_3_points(p1, p2, p3):
    a = det(p1, p2, p3)
    b = dets(p1, p2, p3)
    sx = detx(p1, p2, p3)
    sy = dety(p1, p2, p3)
    c = Point(sx/a/2, sy/a/2)
    return Circle(c, (b/a + sq_dist(c))**.5)


def circle_decide_3_points(p1, p2, p3):
    ps = {p1, p2, p3}
    for p in ps:
        circle = circle_from_2_points(*ps-{p})
        if p in circle:
            return circle
    return circle_from_3_points(p1, p2, p3)


def mincircle2p(points, p1, p2):
    circle = Circle.from_arc(p1, p2)
    for i, p in enumerate(points):
        if p not in circle:
            circle = Circle.from_arc(p1, p2, p)
    return circle


def mincircle1p(points, p1):
    circle = Circle.from_arc(p1)
    ps = shuffled(points)
    for i, p in enumerate(ps):
        if p not in circle:
            circle = mincircle2p(set(ps[:i]), p1, p)
    return circle


def mincircle(points):
    circle = Circle()
    ps = shuffled(points)
    for i, p in enumerate(ps):
        if p not in circle:
            circle = mincircle1p(set(ps[:i]), p)
    return circle


def main():
    for t in count(1):
        n = int(input())
        if n == 0:
            break
        points = [Point.from_spec(input()) for _ in range(n)]
        ans = mincircle(points)
        print('Instancia {}'.format(t))
        print('{:.2f} {:.2f} {:.2f}'.format(ans.c.x, ans.c.y, ans.r))
        print()


if __name__ == '__main__':
    main()
