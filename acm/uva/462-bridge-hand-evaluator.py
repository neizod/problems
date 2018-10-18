#!/usr/bin/env python3


def by_suits(cards):
    suits = {s: [] for s in 'SHDC'}
    for n, s in cards:
        suits[s] += [n]
    return suits


def is_stopped(suit):
    if 'A' in suit:
        return True
    if 'K' in suit and 2 <= len(suit):
        return True
    if 'Q' in suit and 3 <= len(suit):
        return True
    return False


def base_point(cards):
    point = 0
    for rank, suit in cards:
        if rank == 'A':
            point += 4
        if rank == 'K':
            point += 3
        if rank == 'Q':
            point += 2
        if rank == 'J':
            point += 1
    return point


def subs_point(suits):
    point = 0
    for cards in suits.values():
        if len(cards) == 1 and 'K' in cards:
            point -= 1
        if 1 <= len(cards) <= 2 and 'Q' in cards:
            point -= 1
        if 1 <= len(cards) <= 3 and 'J' in cards:
            point -= 1
    return point


def adds_point(suits):
    point = 0
    for cards in suits.values():
        if len(cards) == 2:
            point += 1
        if 0 <= len(cards) <= 1:
            point += 2
    return point


def longest(suits):
    most = -1
    pref = '?'
    for suit, cards in reversed(sorted(suits.items())):
        if most < len(cards):
            most = len(cards)
            pref = suit
    return pref


def bidding(cards):
    suits = by_suits(cards)
    base = base_point(cards)
    subs = subs_point(suits)
    adds = adds_point(suits)
    if base + subs + adds < 14:
        return 'PASS'
    if base + subs >= 16 and all(is_stopped(suit) for suit in suits.values()):
        return 'BID NO-TRUMP'
    return 'BID {}'.format(longest(suits))


def main():
    try:
        while True:
            cards = input().split()
            print(bidding(cards))
    except EOFError:
        pass


if __name__ == '__main__':
    main()
