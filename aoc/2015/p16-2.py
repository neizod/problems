#!/usr/bin/env python3

import re


TAPE = { 'children': 3,
         'cats': 7,
         'samoyeds': 2,
         'pomeranians': 3,
         'akitas': 0,
         'vizslas': 0,
         'goldfish': 5,
         'trees': 3,
         'cars': 2,
         'perfumes': 1 }


def is_sue(features):
    for feature, amount in features.items():
        if feature in {'cats', 'trees'}:
            if not TAPE[feature] < amount:
                return False
        elif feature in {'pomeranians', 'goldfish'}:
            if not TAPE[feature] > amount:
                return False
        else:
            if not TAPE[feature] == amount:
                return False
    return True


def find_aunt(sues):
    for number, features in sues.items():
        if (is_sue(features)):
            return number


def main():
    try:
        sues = {}
        while True:
            number, info = re.findall(r'^Sue (\d+): (.*)$', input().strip())[0]
            sues[int(number)] = {k: int(v) for e in info.split(', ') for k, v in [e.split(': ')]}
    except EOFError:
        print(find_aunt(sues))


if __name__ == '__main__':
    main()
