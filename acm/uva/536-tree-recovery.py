#!/usr/bin/env python3


class Node(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def postorder(self):
        if self.left is not None:
            yield from self.left.postorder()
        if self.right is not None:
            yield from self.right.postorder()
        yield self.value


def recovery(preord, inord, seen=None):
    if seen is None:
        seen = set()
    if preord:
        node = Node(preord.pop())
        seen |= {node.value}
        if inord[-1] != node.value:
            node.left = recovery(preord, inord, seen)
        if inord[-1] == node.value:
            inord.pop()
        if inord and inord[-1] not in seen:
            node.right = recovery(preord, inord, seen)
    return node


def main():
    try:
        while True:
            preord, inord = input().split()
            tree = recovery(list(preord[::-1]), list(inord[::-1]))
            print(''.join(tree.postorder()))
    except EOFError:
        pass


if __name__ == '__main__':
    main()
