#!/usr/bin/env python3

from collections import Counter


def move_direction(moves):
    furthest = 0
    length = {'n': 0, 'ne': 0, 'nw': 0}
    for move in moves:
        if move == 'n':
            length['n'] += 1
        elif move == 's':
            length['n'] -= 1
        elif move == 'ne':
            length['ne'] += 1
        elif move == 'sw':
            length['ne'] -= 1
        elif move == 'nw':
            length['nw'] += 1
        elif move == 'se':
            length['nw'] -= 1
        furthest = max(furthest, find_length(**length))
    return furthest


def find_length(n, ne, nw):
    return sum(sorted([abs(n), abs(ne), abs(nw)], reverse=True)[:2])


def reduce_direction(moves):
    count = Counter(moves)
    n = count['n'] - count['s']
    ne = count['ne'] - count['sw']
    nw = count['nw'] - count['se']
    return find_length(n, ne, nw)


def main():
    print(move_direction(input().split(',')))


if __name__ == '__main__':
    main()
