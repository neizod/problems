#!/usr/bin/env python3


def fill(ls, capacity, config=None):
    if capacity == 0:
        return [config]
    if not ls or capacity < 0:
        return []
    if config is None:
        config = []
    return fill(ls[:-1], capacity, config) + fill(ls[:-1], capacity-ls[-1], config+[ls[-1]])


def main():
    try:
        capacity = 150
        ls = []
        while True:
            ls += [int(input())]
    except EOFError:
        it = fill(ls, capacity)
        smallest = min(len(i) for i in it)
        print(sum(len(i) == smallest for i in it))


if __name__ == '__main__':
    main()
