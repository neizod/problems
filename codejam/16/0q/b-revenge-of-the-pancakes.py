#!/usr/bin/env python3

def tail(iterable):
    iterator = iter(iterable)
    next(iterator)
    return iterator


def flip(pancakes):
    return sum(p != q for p, q in zip(pancakes, tail(pancakes)))


def main():
    for case in range(int(input())):
        pancakes = input().strip() + '+'
        print('Case #{}: {}'.format(case+1, flip(pancakes)))


if __name__ == '__main__':
    main()
