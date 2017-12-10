#!/usr/bin/env python3

'''
(!) Note: This Python solution is **NOT** fast enough to pass the test.
	  The same algorithm in C++, however, will pass them in a breeze.
'''


from enum import Enum
from itertools import count


class Notation(str, Enum):
    WHITE = '-'
    BLACK = '#'


class Triangle(object):
    def __init__(self, layout):
        self.layout = layout

    def has_coord(self, x, y):
        return 0 <= y < len(self.layout) and 0 <= x < len(self.layout[y])

    def iter_expand_down(self, x, y, size):
        if not self.has_coord(x, y+size):
            yield Notation.BLACK
        else:
            yield self.layout[y+size][x]
            for dy in reversed(range(size)):
                px = 2*(size-dy) - 1
                for dx in range(2):
                    yield self.layout[y+dy][x+px+dx]

    def iter_expand_up(self, x, y, size):
        if not self.has_coord(x, y+size) or not self.has_coord(x-2*size, y+size):
            yield Notation.BLACK
        else:
            for dx in reversed(range(2*size+1)):
                yield self.layout[y+size][x-dx]

    def find_largest(self, expand_method, x, y, size=0):
        if all(piece == Notation.WHITE for piece in expand_method(x, y, size)):
            return self.find_largest(expand_method, x, y, size+1)
        return size

    def largest_sub_triangle(self):
        answers = []
        for y, _ in enumerate(self.layout):
            for x, _ in enumerate(self.layout[y]):
                if x%2 == 0:
                    answers += [self.find_largest(self.iter_expand_down, x, y)]
                else:
                    answers += [self.find_largest(self.iter_expand_up, x, y)]
        return max(answers)**2


def main():
    for test in count(1):
        n = int(input())
        if n == 0:
            break
        triangle = Triangle([input().strip() for _ in range(n)])
        answer = triangle.largest_sub_triangle()
        print('Triangle #{}\nThe largest triangle area is {}.\n'.format(test, answer))


if __name__ == '__main__':
    main()
