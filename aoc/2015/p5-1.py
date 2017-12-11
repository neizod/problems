#!/usr/bin/env python3

from collections import Counter


def is_nice(word):
    if not sum(c in 'aeiou' for c in word) >= 3:
        return False
    if not any(s == t for s, t in zip(word, word[1:])):
        return False
    if any(piece in word for piece in ['ab', 'cd', 'pq', 'xy']):
        return False
    return True


def main():
    try:
        count = 0
        while True:
            word = input().strip()
            count += is_nice(word)
    except EOFError:
        print(count)


if __name__ == '__main__':
    main()
