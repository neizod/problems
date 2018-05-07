#!/usr/bin/env python3


def main():
    for _ in range(int(input())):
        n = int(input())
        ls = {n: 0 for n in range(n)}
        for _ in range(n):
            _, *ps = [int(i) for i in input().split()]
            ps = set(ps)
            for p in ps:
                if p in ls:
                    ls[p] += 1
            avail = sorted([(v, k) for k, v in ls.items() if k in ps])
            if not avail:
                print(-1)
            else:
                which = avail[0][1]
                print(which)
                del ls[which]


if __name__ == '__main__':
    main()
