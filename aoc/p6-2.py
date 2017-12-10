#!/usr/bin/env python3


def main():
    ls = [int(n) for n in input().split()]
    seen = {}
    c = 0
    while str(ls) not in seen:
        seen[str(ls)] = c
        i = ls.index(max(ls))
        d, m = divmod(ls[i], len(ls))
        ls[i] = 0
        for j in range(1+i-len(ls), 1+i):
            if m > 0:
                ls[j] += d + 1
            else:
                ls[j] += d
            m -= 1
        c += 1
    print(c - seen[str(ls)])


if __name__ == '__main__':
    main()
