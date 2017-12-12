#!/usr/bin/env python3

from itertools import permutations


class Node(object):
    def __init__(self, name):
        self.name = name
        self.neighbor = {}

    def add_neighbor(self, other, distant):
        if isinstance(other, Node):
            other = other.name
        self.neighbor[other] = distant

    def distant(self, other):
        if isinstance(other, Node):
            other = other.name
        if other not in self.neighbor:
            return None
        return self.neighbor[other]


def main():
    try:
        graph = {}
        while True:
            relation, raw_distant = input().split(' = ')
            distant = int(raw_distant)
            city1, city2 = relation.split(' to ')
            if city1 not in graph:
                graph[city1] = Node(city1)
            if city2 not in graph:
                graph[city2] = Node(city2)
            graph[city1].add_neighbor(city2, distant)
            graph[city2].add_neighbor(city1, distant)
    except EOFError:
        lengths = []
        for cities in permutations(graph.values()):
            length = 0
            for city1, city2 in zip(cities, cities[1:]):
                if city1.distant(city2) is None:
                    break
                length += city1.distant(city2)
            else:
                lengths += [length]
        print(min(lengths))


if __name__ == '__main__':
    main()
