#!/usr/bin/env python3


class Node(object):
    def __init__(self, name):
        self.name = name
        self.flooded = False
        self.neighbors = {}

    def add_neighbor(self, other):
        self.neighbors[other.name] = other

    def flood(self):
        if self.flooded:
            return
        self.flooded = True
        for neighbor in self.neighbors.values():
            neighbor.flood()


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
        nodes['0'].flood()
        print(sum(node.flooded for node in nodes.values()))


if __name__ == '__main__':
    main()
