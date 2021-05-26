#!/usr/bin/env python3


def reversort_weight(xs):
    weight = 0
    i = 0
    while i < len(xs) - 1:
        j = xs.index(i+1) + 1
        weight += len(xs[i:j])
        xs[i:j] = xs[i:j][::-1]
        i += 1
    return weight


def main():
    for case in range(int(input())):
        _ = input()
        xs = [int(x) for x in input().split()]
        answer = reversort_weight(xs)
        print(f'Case #{case+1}: {answer}')


if __name__ == '__main__':
    main()
