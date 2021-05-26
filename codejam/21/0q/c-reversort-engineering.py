#!/usr/bin/env python3


def reversort_example(n, c):
    if c < n-1 or c > n*(n+1)/2-1:
        return None
    xs = [1 for _ in range(n)]
    xs[-1] = 0
    c -= sum(xs)
    for i in range(n-1):
        if c <= 0:
            break
        avail = n - i - xs[i]
        xs[i] += min(avail, c)
        c -= min(avail, c)
    ws = [n]
    for i in reversed(range(n-1)):
        ws += [i+1]
        ws[-xs[i]:] = ws[-xs[i]:][::-1]
    return ws[::-1]


def main():
    for case in range(int(input())):
        n, c = [int(x) for x in input().split()]
        answer = reversort_example(n, c) or 'IMPOSSIBLE'
        print(f'Case #{case+1}: {answer}')


if __name__ == '__main__':
    main()
