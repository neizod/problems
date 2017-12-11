#!/usr/bin/env python3

from collections import Counter


class Node(object):
    def __init__(self, name, raw_weight, deferred_childs=None):
        self.name = name
        self.weight = int(raw_weight.strip('()'))
        self.total_weight = 0
        self.childs = []
        self.deferred_childs = deferred_childs or []

    def __repr__(self):
        return '{} ({}, {})'.format(self.name, self.weight, self.total_weight)

    def fix_total_weight(self, weight):
        self.weight -= self.total_weight - weight

    def calc_total_weight(self):
        self.total_weight = self.weight
        for child in self.childs:
            self.total_weight += child.calc_total_weight()
        return self.total_weight

    def find_diff_child(self):
        count = Counter(child.total_weight for child in self.childs)
        if len(count) <= 1:
            return None, None
        for child in self.childs:
            if child.total_weight == count.most_common()[1][0]:
                return child, count.most_common()[0][0]

    def traverse_wrong_weight(self, node=None, correct=None):
        child, weight = self.find_diff_child()
        if child:
            return child.traverse_wrong_weight(child, weight)
        return node, correct

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
        root = Node.make_hierarchy(nodes)
        root.calc_total_weight()
        node, correct = root.traverse_wrong_weight()
        node.fix_total_weight(correct)
        print(node.weight)


if __name__ == '__main__':
    main()
