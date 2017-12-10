#!/usr/bin/env python3


def twist(ls, index, size):
    if index+size <= len(ls):
        ls[index:index+size] = list(reversed(ls[index:index+size]))
    else:
        front = (index+size) % len(ls)
        split = len(ls) - index
        tmp = list(reversed(ls[index:]+ls[:front]))
        ls[index:] = tmp[:split]
        ls[:front] = tmp[split:]
    return ls


def solve(ts):
    skip = 0
    index = 0
    ls = list(range(256))
    for size in ts:
        ls = twist(ls, index, size)
        index += size + skip
        index %= len(ls)
        skip += 1
    return ls


def main():
    ts = [int(n) for n in input().split(',')]
    ls = solve(ts)
    print(ls[0] * ls[1])


if __name__ == '__main__':
    main()
