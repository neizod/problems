#!/usr/bin/env python3

from math import factorial


def main():
    try:
        while True:
            n = int(input())
            print('{}!'.format(n))
            print(factorial(n))
    except EOFError:
        pass


if __name__ == '__main__':
    main()
