#!/usr/bin/env python3


def fill(ls, capacity):
    if capacity == 0:
        return 1
    if not ls or capacity < 0:
        return 0
    return fill(ls[:-1], capacity) + fill(ls[:-1], capacity-ls[-1])


def main():
    try:
        capacity = 150
        ls = []
        while True:
            ls += [int(input())]
    except EOFError:
        ls.sort()
        print(fill(ls, capacity))


if __name__ == '__main__':
    main()
