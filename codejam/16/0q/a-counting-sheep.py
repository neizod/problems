#!/usr/bin/env python3

def counting_sheep(initial):
    if initial == 0:
        return None
    unseen = {number for number in range(10)}
    multiplier = 0
    while unseen:
        multiplier += 1
        unseen -= {int(digit) for digit in str(multiplier * initial)}
    return multiplier * initial


def main():
    for case in range(int(input())):
        final = counting_sheep(int(input())) or 'INSOMNIA'
        print('Case #{}: {}'.format(case+1, final))


if __name__ == '__main__':
    main()
