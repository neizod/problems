#!/usr/bin/env python3

from collections import defaultdict


def main():
    dictionary = defaultdict(list)
    while True:
        string = input()
        if string == '#':
            break
        for word in string.split():
            index = ''.join(sorted(word.lower()))
            dictionary[index] += [word]
    for word in sorted(ws[0] for ws in dictionary.values() if len(ws) == 1):
        print(word)


if __name__ == '__main__':
    main()
