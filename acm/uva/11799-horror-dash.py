#!/usr/bin/env python3


def main():
    for c in range(int(input())):
        _, *ns = [int(n) for n in input().split()]
        print('Case {}: {}'.format(c+1, max(ns)))


if __name__ == '__main__':
    main()
