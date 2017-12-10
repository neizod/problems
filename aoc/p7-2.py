#!/usr/bin/env python3


class Node(object):
    def __init__(self, name, raw_weight, deferred_childs=None):
        self.name = name
        self.weight = int(raw_weight.strip('()'))
        self.total_weight = 0
        self.childs = []
        self.deferred_childs = deferred_childs or []

    def __repr__(self):
        return '{} ({}, {})'.format(self.name, self.weight, self.total_weight)

    def calc_total_weight(self):
        self.total_weight = self.weight
        for child in self.childs:
            self.total_weight += child.calc_total_weight()
        return self.total_weight

    def traverse_wrong_weight(self, answers=None):
        if answers is None:
            answers = []
        if self.childs and len({child.total_weight for child in self.childs}) != 1:
            answers += [self]
        for child in self.childs:
            child.traverse_wrong_weight(answers)
        return answers

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
        return Node.make_hierarchy(nodes)


def interact_solve(root):
    root.calc_total_weight()
    answers = root.traverse_wrong_weight()
    wrong = answers[-1].childs[3]
    wrong.weight -= 5
    root.calc_total_weight()
    if root.traverse_wrong_weight():
        raise ValueError('fix wrong node')
    print(wrong)


if __name__ == '__main__':
    root = main()
    interact_solve(root)
