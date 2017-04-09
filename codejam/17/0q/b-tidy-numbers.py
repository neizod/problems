#!/usr/bin/env python3

from itertools import count


def is_tidy(string):
    return all(before <= after for before, after in zip(string, string[1:]))


def last_tidy(string):
    for length in count(2):
        if length > len(string):
            return string
        tail_digits = string[-length:]
        if not is_tidy(tail_digits):
            length -= 1
            tail_adjust = string[:-length] + ('0'*(length))
            string = str(int(tail_adjust)-1)


def main():
    for case in range(int(input())):
        print('Case #{}: {}'.format(case+1, last_tidy(input())))


if __name__ == '__main__':
    main()
