#!/usr/bin/env python3


class Node(object):
    def __init__(self, char, val=0):
        self.char = char
        self.leaf = {}
        self.val = val

    def __repr__(self):
        if not self.leaf:
            return '{' + repr(self.char) + '}'
        return '(' + repr(self.char) + ',' + str(self.val) + ',' + str(list(self.leaf.values())) + ')'

    def add(self, word):
        if not word:
            return
        head, *rests = word
        if head not in self.leaf:
            self.leaf[head] = Node(head)
        self.leaf[head].add(rests)

    def eval(self):
        if not self.leaf:
            self.val = 1
        else:
            self.val = sum(leaf.eval() for leaf in self.leaf.values())
        return self.val


def make_tree(words):
    root = Node('')
    for word in words:
        root.add(word)
    root.eval()
    return root


def prod(pool, out=1):
    for lvl in pool:
        out *= len(lvl)
    return out


def new_word(node, pool):
    if node.val == prod(pool):
        return '-'
    def aux(node, pool):
        head, *rests = pool
        if not rests:
            out = head - set(node.leaf)
            return out.pop()
        prod_rests = prod(rests)
        for h in head:
            if h not in node.leaf:
                node.leaf[h] = Node(h)
            if node.leaf[h].val < prod_rests:
                return h + aux(node.leaf[h], rests)
    return aux(node, pool)


def create_new_word(words, length):
    pool = [{word[i] for word in words} for i in range(length)]
    root = make_tree(words)
    return new_word(root, pool)


def main():
    for case in range(int(input())):
        no_words, length = [int(n) for n in input().split()]
        words = [input().strip() for _ in range(no_words)]
        answer = create_new_word(words, length)
        print('Case #{}: {}'.format(case+1, answer))


if __name__ == '__main__':
    main()
