#!/usr/bin/env python3


def analyse(a, b):
    x, p = divmod(a+b, 2)
    if p == 1:
        return None
    y = a - x
    if y < 0:
        return None
    return x, y


def main():
    for _ in range(int(input())):
        a, b = [int(n) for n in input().split()]
        answer = analyse(a, b)
        if answer is None:
            print('impossible')
        else:
            print('{} {}'.format(*answer))


if __name__ == '__main__':
    main()
