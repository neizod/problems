#!/usr/bin/env python3


def point(card):
    rank, suit = card
    if not rank.isdigit():
        return 10
    return int(rank)


def main():
    for c in range(int(input())):
        deck = []
        while len(deck) < 52:
            deck += input().split()
        rest, hand = deck[:-25], deck[-25:]
        y = 0
        for _ in range(3):
            x = point(rest.pop())
            for _ in range(10-x):
                rest.pop()
            y += x
        rest += hand
        print('Case {}: {}'.format(c+1, rest[y-1]))
    pass


if __name__ == '__main__':
    main()
