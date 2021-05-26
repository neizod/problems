#!/usr/bin/env python3

def solve(n, xs):
    c = 0
    ys = [xs[0]]
    for i in range(n-1):
        ma = str(int(ys[i])+1)
        ob = xs[i+1]
        mb = ob
        if all(a == b for a, b in zip(ma, ob)):
            mb = ma
        while int(mb) < int(ma):
            mb += '0'
        ys += [mb]
        c += len(mb) - len(ob)
    return c


def main():
    for case in range(int(input())):
        n = int(input())
        xs = input().split()
        answer = solve(n, xs)
        print(f'Case #{case+1}: {answer}')


if __name__ == '__main__':
    main()
