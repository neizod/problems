#!/usr/bin/env python3


def min_cost(cj, jc, pattern):
    cost = {'CC': 0, 'JJ': 0, 'CJ': cj, 'JC': jc}
    return sum(cost[pattern.replace('?', '')[i:i+2]] for i in range(len(pattern)-1))


def main():
    for case in range(int(input())):
        rcj, rjc, pattern = input().split()
        answer = min_cost(int(rcj), int(rjc), pattern)
        print(f'Case #{case+1}: {answer}')


if __name__ == '__main__':
    main()
