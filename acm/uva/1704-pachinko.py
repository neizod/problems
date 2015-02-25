#!/usr/bin/env python3

from numpy import matrix, zeros


class RandomWalk(object):

    limpow = 10**9
    offset = [(0,-1), (0,1), (-1,0), (1,0)]

    def movable(self, x, y):
        return self.inner(x, y) and not self.blocked(x, y)

    def blocked(self, x, y):
        return self.grid[y][x] == 'X'

    def inner(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def iter_moves(self, x, y):
        for p, (i, j) in zip(self.prob, self.offset):
            yield p, i, j

    def adjacency(self, node, i, j):
        return node + i + j*self.width

    def destination(self, node, x, y, i, j):
        return self.adjacency(node, i, j) if self.movable(x+i, y+j) else node

    def make_adjmatrix(self):
        node = 0
        adjmatrix = matrix(zeros([self.height*self.width]*2, float))
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == 'T':
                    adjmatrix[node,node] = 1
                elif cell == '.':
                    for p, i, j in self.iter_moves(x, y):
                        dest = self.destination(node, x, y, i, j)
                        adjmatrix[node,dest] += p
                node += 1
        return adjmatrix

    def __call__(self, power=limpow):
        head = [cell == '.' for cell in next(iter(self.grid))]
        head = [cell/sum(head) for cell in head]
        init = matrix(head + [0] * self.width * (self.height-1))
        return next(iter((init * self.adjmatrix**power).tolist()))

    def __init__(self, grid, prob, width, height):
        self.grid = grid
        self.prob = prob
        self.width = width
        self.height = height
        self.adjmatrix = self.make_adjmatrix()


def main():
    w, h = [int(i) for i in input().split()]
    prob = [int(i)/100 for i in input().split()]
    grid = [input().strip() for _ in range(h)]

    random_walk = RandomWalk(grid, prob, w, h)
    for answer in random_walk():
        if answer != 0:
            print('{:.9f}'.format(answer))


if __name__ == '__main__':
    main()
