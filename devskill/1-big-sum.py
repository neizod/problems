#!/usr/bin/env python3

from itertools import zip_longest


# XXX another ill-posed problem that fail to describe what its really need...
#     the constrain says it will not give any number with leading zeros,
#     but what about trailing zeros? what's the rule to handle them!?
#
#     suppose that we gets "400,300", what's an answer?
#     first interpretation is:
#     rev(400) = 004 = 4, rev(300) = 003 = 3, so the output must be 7, right?
#     WRONG!!
#     the correct answer will be:
#     rev(400) = 004, rev(300) = 003, and the sums is 007,
#     thus the output must be rev(007) = 700!!!
#     WTF with this logic!??
def fuck_sum(digits1, digits2):
    carry = 0
    digits3 = []
    for d1, d2 in zip_longest(digits1, digits2, fillvalue='0'):
        carry, d3 = divmod(int(d1)+int(d2)+carry, 10)
        digits3 += [d3]
    if carry:
        digits3 += [carry]
    return int(''.join(str(digit) for digit in digits3))


def main():
    try:
        while True:
            digits1, digits2 = input().split(',')
            print(fuck_sum(digits1, digits2))
            # XXX why not just this straightforward implementation??
            # print(int(str(int(digits1[::-1])+int(digits2[::-1]))[::-1]))
    except EOFError:
        pass


if __name__ == '__main__':
    main()
