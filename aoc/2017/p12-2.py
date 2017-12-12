#!/usr/bin/env python3


class Node(object):
    def __init__(self, name):
        self.name = name
        self.group = None
        self.neighbors = {}

    def add_neighbor(self, other):
        self.neighbors[other.name] = other

    def flood(self, group):
        if self.group is not None:
            return
        self.group = group
        for neighbor in self.neighbors.values():
            neighbor.flood(group)


def main():
    try:
        nodes = {}
        while True:
            name, others = input().split(' <-> ')
            if name not in nodes:
                nodes[name] = Node(name)
            others = others.split(', ')
            for other in others:
                if other not in nodes:
                    nodes[other]  = Node(other)
                nodes[name].add_neighbor(nodes[other])
                nodes[other].add_neighbor(nodes[name])
    except EOFError:
        group = 0
        for node in nodes.values():
            if node.group is None:
                node.flood(group)
                group += 1
        print(group)


if __name__ == '__main__':
    main()
