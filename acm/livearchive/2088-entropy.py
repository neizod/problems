#!/usr/bin/env python3

from collections import Counter


class Node(object):
    def is_terminated(self):
        return self.left is None and self.right is None

    def total(self, depth=0):
        if self.is_terminated():
            if depth == 0:
                depth = 1
            return self.value * depth
        return self.left.total(depth+1) + self.right.total(depth+1)

    @classmethod
    def from_leaves(cls, left, right):
        return cls('', left.value + right.value, left, right)

    def __init__(self, symbol='', value=0, left=None, right=None):
        self.symbol = symbol
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        if self.is_terminated():
            return 'Node({!r}, {})'.format(self.symbol, self.value)
        return 'Node({!r}, {}, {!r}, {!r})'.format( self.symbol, self.value,
                                                    self.left,   self.right )

    def __lt__(self, other):
        return self.value < other.value


def make_tree(queue):
    import heapq as hq
    queue = queue[:]
    hq.heapify(queue)
    while len(queue) > 1:
        left = hq.heappop(queue)
        right = hq.heappop(queue)
        hq.heappush(queue, Node.from_leaves(left, right))
    return queue.pop()


def main():
    while True:
        raw = input().strip()
        if raw == 'END':
            break
        tree = make_tree([Node(k, v) for k, v in Counter(raw).most_common()])
        full = 8 * tree.value
        entropy = tree.total()
        print('{} {} {:.1f}'.format(full, entropy, full/entropy))


if __name__ == '__main__':
    main()
