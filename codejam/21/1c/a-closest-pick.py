#!/usr/bin/env python3


def single_strategy(k, xs):
    ys = [xs[0]-1, k-xs[-1]]
    ys += [(b-a)//2 for a, b in zip(xs, xs[1:])]
    ys.sort()
    return sum(ys[-2:])


def double_strategy(k, xs):
    if len(xs) == 1:
        return 0
    return max(b-a-1 for a, b in zip(xs, xs[1:]))


def optimize_ticket(k, xs):
    xs = sorted(set(xs))
    m = max(single_strategy(k, xs), double_strategy(k, xs))
    return m/k


def main():
    for t in range(int(input())):
        _, k = [int(x) for x in input().split()]
        xs = [int(x) for x in input().split()]
        answer = optimize_ticket(k, xs)
        print(f'Case #{t+1}: {answer}')


if __name__ == '__main__':
    main()
