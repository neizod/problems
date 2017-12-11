#!/usr/bin/env python3


class Node(object):
    def __init__(self, name, raw_weight, deferred_childs=None):
        self.name = name
        self.weight = int(raw_weight.strip('()'))
        self.childs = []
        self.deferred_childs = deferred_childs or []

    def __repr__(self):
        return '{} ({})'.format(self.name, self.weight)

    @classmethod
    def make_hierarchy(cls, nodes):
        memo = {node.name: node for node in nodes}
        has_parents = {node.name: False for node in nodes}
        for node in nodes:
            for name in node.deferred_childs:
                node.childs += [memo[name]]
                has_parents[name] = True
            node.deferred_childs = []
        if sum(not has_parent for has_parent in has_parents.values()) != 1:
            raise ValueError('multiple root nodes')
        for name, has_parent in has_parents.items():
            if not has_parent:
                return memo[name]


def main():
    try:
        nodes = []
        while True:
            line = input().replace('->','').replace(',', '')
            name, raw_weight, *deferred_childs = line.split()
            nodes += [Node(name, raw_weight, deferred_childs)]
    except EOFError:
        print(Node.make_hierarchy(nodes))


if __name__ == '__main__':
    main()
