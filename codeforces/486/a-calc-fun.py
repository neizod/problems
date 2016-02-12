#!/usr/bin/env python3


def f(n):
    return (1 if n % 2 == 0 else -1) * (n+1) // 2


def main():
    print(f(int(input())))


if __name__ == '__main__':
    main()
