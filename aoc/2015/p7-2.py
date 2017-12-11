#!/usr/bin/env python3

from operator import and_, or_, add, sub, lshift, rshift, inv


class Node(object):
    def __init__(self, name, inst=None, left='0', right='0', value=0, stable=False):
        self.name = name
        self.value = value
        self.inst = inst
        self.left = left
        self.right = right
        self.stable = stable

    @classmethod
    def fix_number(cls, name):
        return cls(name, value=int(name), stable=True)


class Circuit(object):
    def __init__(self):
        self.nodes = {}

    def __getitem__(self, name):
        if name.isdigit():
            return Node.fix_number(name)
        return self.nodes[name]

    def add_reg(self, name, inst, left, right):
        self.nodes[name] = Node(name, inst, left, right)

    def get(self, node):
        if isinstance(node, str):
            node = self[node]
        if node.stable:
            return node.value
        node.stable = True
        node.value = node.inst(self.get(node.left), self.get(node.right)) % 2**16
        return node.value

    def set(self, pairs, reset=True):
        for node, value in pairs.items():
            if isinstance(node, str):
                node = self[node]
            node.value = value
        if reset:
            self.reset(pairs.keys())

    def reset(self, ignores=None):
        for name, node in self.nodes.items():
            if ignores and name not in ignores:
                node.stable = False


def decode(code):
    *rest, reg2, _, target = code
    if len(code) == 3:
        reg1 = '0'
        inst = add
    elif len(code) == 4:
        reg1 = str(-1%2**16)
        inst = sub
    elif len(code) == 5:
        reg1, raw_inst = rest
        if raw_inst == 'AND':
            inst = and_
        if raw_inst == 'OR':
            inst = or_
        if raw_inst == 'LSHIFT':
            inst = lshift
        if raw_inst == 'RSHIFT':
            inst = rshift
    return inst, reg1, reg2, target


def main():
    try:
        circuit = Circuit()
        while True:
            inst, reg1, reg2, target = decode(input().split())
            circuit.add_reg(target, inst, reg1, reg2)
    except EOFError:
        print(circuit.get('a'))
        circuit.set({'b': circuit.get('a')})
        print(circuit.get('a'))


if __name__ == '__main__':
    main()
