#!/usr/bin/env python3

from collections import defaultdict


def main():
    the_list = defaultdict(list)
    for _ in range(int(input())):
        country, name = input().split(maxsplit=1)
        the_list[country] += [name]
    for country, names in sorted(the_list.items()):
        print(country, len(names))


if __name__ == '__main__':
    main()
