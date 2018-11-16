#!/usr/bin/env python3


def main():
    for _ in range(int(input())):
        n, dist = [int(i) for i in input().split()]
        count = 0
        for _ in range(n):
            speed, fuel, rate = [int(i) for i in input().split()]
            count += (fuel >= rate*dist/speed)
        print(count)


if __name__ == '__main__':
    main()
