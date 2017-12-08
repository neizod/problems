#!/usr/bin/env python3

'''
(!) Note: This Python solution is **NOT** fast enough to pass the test.
	  The same algorithm in C++, however, will pass them in a breeze.
'''


class MineGrid(object):
    def __init__(self, hint):
        self.hint = hint
        self.width = len(hint[0])
        self.height = len(hint)
        self.mine = [[None for _ in range(self.width)] for _ in range(self.height)]

    @classmethod
    def solve(cls, hint):
        self = cls(hint)
        self.mine_from_hint()
        return self.mine

    def iter_suround(self, x, y):
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if (dx, dy) == (0, 0):
                    continue
                if 0 <= x+dx < self.width and 0 <= y+dy < self.height:
                    yield x+dx, y+dy

    def count_suround_mines(self, x, y):
        return sum(self.mine[gy][gx] is None for gx, gy in self.iter_suround(x, y))

    def update_mine(self, is_mine, x, y):
        if is_mine:
            self.mine[y][x] = 'L'
            self.hint[y][x] -= 4
            for gx, gy in self.iter_suround(x, y):
                self.hint[gy][gx] -= 1
        else:
            self.mine[y][x] = '-'

    def revealed_cell(self, x, y):
        return self.mine[y][x] is not None

    def mine_from_hint(self):
        for y in range(self.height):
            while None in self.mine[y]:
                for x in range(self.width):
                    if self.revealed_cell(x, y):
                        continue
                    if self.hint[y][x] < 4:
                        self.update_mine(False, x, y)
                    if self.hint[y][x] > self.count_suround_mines(x, y):
                        self.update_mine(True, x, y)


if __name__ == '__main__':
    for _ in range(int(input())):
        n_row, _ = [int(n) for n in input().split()]
        hint = [[int(n) for n in input().split()] for _ in range(n_row)]
        for line in MineGrid.solve(hint):
            print(''.join(c for c in line))
