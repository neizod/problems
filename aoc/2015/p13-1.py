#!/usr/bin/env python3

import re
from itertools import permutations


def get_pair(persons, a, b):
    return persons[a][b]+persons[b][a]


def calc_happiness(persons, sitting):
    return sum(get_pair(persons, a, b) for a, b in zip(sitting, sitting[1:]+sitting[:1]))


def maximize_happiness(persons):
    return max(calc_happiness(persons, sitting) for sitting in  permutations(persons))


def main():
    try:
        persons = {}
        while True:
            name, sign, raw_value, other = re.findall(r'^(\w+).*? (gain|lose) (\d+).*?(\w+)\.$', input())[0]
            value = int(raw_value) * (-1 if sign == 'lose' else 1)
            if name not in persons:
                persons[name] = {}
            persons[name][other] = value
    except EOFError:
        print(maximize_happiness(persons))


if __name__ == '__main__':
    main()
