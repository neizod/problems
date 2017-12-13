#!/usr/bin/env python3

import re
from operator import add, mul
from functools import reduce


def transpose(matrix):
    return list(zip(*matrix))


def value_each(ingredients, amonts):
    return [[i*a for i in ingradient] for ingradient, a in zip(ingredients, amonts)]


def sum_values(ingredients, amonts):
    return [max(0, sum(feature)) for feature in transpose(value_each(ingredients, amonts))]


def calc_score(ingredients, amonts):
    return reduce(mul, sum_values(ingredients, amonts))


def iter_sumto(limit, n=2):
    if n == 0:
        raise ValueError
    if n == 1:
        yield (limit,)
    else:
        for head in range(limit+1):
            for rest in iter_sumto(limit-head, n-1):
                yield (head, *rest)


def main():
    try:
        ingredients = []
        while True:
            name, *numbers = re.findall(r'(\w+):.*?(-?\d+).*?(-?\d+).*?(-?\d+).*?(-?\d+).*?(-?\d+)', input())[0]
            capacity, durability, flavor, texture, calories = [int(n) for n in numbers]
            ingredients += [[capacity, durability, flavor, texture]]
    except EOFError:
        limit = 100
        print(max(calc_score(ingredients, amonts) for amonts in iter_sumto(limit, len(ingredients))))


if __name__ == '__main__':
    main()
