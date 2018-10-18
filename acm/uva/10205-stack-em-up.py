#!/usr/bin/env python3


def init_deck():
    return [ '{} of {}'.format(r, s)
                 for s in 'Clubs Diamonds Hearts Spades'.split()
                 for r in '2 3 4 5 6 7 8 9 10 Jack Queen King Ace'.split() ]


def shuff(deck, final):
    out = [None for _ in range(52)]
    for idx, pos in enumerate(final):
        out[idx] = deck[pos]
    return out


def main():
    cases = int(input())
    input()
    while cases:
        cases -= 1
        deck = init_deck()
        moves = []
        for _ in range(int(input())):
            move = []
            while len(move) < 52:
                move += [int(n)-1 for n in input().split()]
            moves += [move]
        try:
            while True:
                k = int(input())
                deck = shuff(deck, moves[k-1])
        except (ValueError, EOFError):
            pass
        for card in deck:
            print(card)
        if cases:
            print()


if __name__ == '__main__':
    main()
