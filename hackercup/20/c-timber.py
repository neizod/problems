#!/usr/bin/env python3


def longest_sequence(logs):
    logs.sort()
    seq = {}
    for pos, height in logs:
        for start, stop in [(pos, pos+height), (pos-height, pos)]:
            if start not in seq:
                seq[start] = 0
            if stop not in seq:
                seq[stop] = seq[start] + height
            else:
                seq[stop] = max(seq[stop], seq[start] + height)
    return max(seq.values())


def main():
    for c in range(int(input())):
        logs = [[int(n) for n in input().split()] for _ in range(int(input()))]
        print(f'Case #{c+1}: {longest_sequence(logs)}')


if __name__ == '__main__':
    main()
