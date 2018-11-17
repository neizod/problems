#!/usr/bin/env python3

def main():
    for _ in range(int(input())):
        c = 0
        for _ in range(2):
            b1, b2, p1, p2 = [int(n) for n in input().split()]
            c += (b1+b2 > p1+p2)
        if c == 2:
            print('Banglawash')
        else:
            print('Miss')


if __name__ == '__main__':
    main()
