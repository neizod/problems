#!/usr/bin/env python3

from collections import deque
from math import isnan


class Node(object):
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None


def read_tree():
    tree = Node()
    while True:
        for pair in input().strip().split():
            if pair == '()':
                return tree
            now = tree
            value, position = pair.strip('()').split(',')
            for direction in position:
                if direction == 'L':
                    if now.left is None:
                        now.left = Node()
                    now = now.left
                else:
                    if now.right is None:
                        now.right = Node()
                    now = now.right
            if now.value is None:
                now.value = int(value)
            else:
                now.value = float('nan')


def traverse(tree):
    values = []
    queue = deque([tree])
    while queue:
        now = queue.popleft()
        if now.left is not None:
            queue.append(now.left)
        if now.right is not None:
            queue.append(now.right)
        values.append(now.value)
    return values


def testcase():
    values = traverse(read_tree())
    if any(value is None or isnan(value) for value in values):
        print('not complete')
    else:
        print(' '.join(str(value) for value in values))


def main():
    try:
        while True:
            testcase()
    except EOFError:
        exit(0)


if __name__ == '__main__':
    main()
