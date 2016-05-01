#!/usr/bin/env python3

def geometric_series(base, power):
    if base == 1:
        return 1
    return (base**power - 1) // (base - 1)


def positions(pattern, complexity):
    base_position = geometric_series(pattern, complexity)
    return [placement*base_position for placement in range(pattern)]


def main():
    for case in range(int(input())):
        pattern, complexity, _ = [int(n) for n in input().split()]
        answer = (pos+1 for pos in positions(pattern, complexity))
        print('Case #{}: {}'.format(case+1, ' '.join(str(n) for n in answer)))


if __name__ == '__main__':
    main()
