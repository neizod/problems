#!/usr/bin/env python3

def flip(pancake):
    return '+' if pancake == '-' else '-'


def flips(pancakes):
    return [flip(pancake) for pancake in pancakes]


def can_flip(pancakes, size):
    pancakes = list(pancakes)
    flip_times = 0
    for start in range(len(pancakes)-size+1):
        if pancakes[start] == '-':
            pancakes[start:start+size] = flips(pancakes[start:start+size])
            flip_times += 1
    if all(pancake == '+' for pancake in pancakes):
        return flip_times
    return 'IMPOSSIBLE'


def main():
    for case in range(int(input())):
        pancakes, raw_k = input().split()
        print('Case #{}: {}'.format(case+1, can_flip(pancakes, int(raw_k))))


if __name__ == '__main__':
    main()
