from fractions import Fraction
from math import factorial

from operator import mul
from functools import reduce

def product(member):
    return reduce(mul, member)

def repile(minimum, remain_piles, remain_dishes, case, stack=[]):
    if remain_piles == 1:
        if remain_dishes >= stack[-1]:
            case.append(stack+[remain_dishes])

    for each in range(minimum, remain_dishes):
        repile(each, remain_piles-1, remain_dishes-each, case, stack+[each])


for test in range(int(input())):
    dishes, least = [int(num) for num in input().split()]
    piles = dishes // least

    every_case = []
    every_case.append([dishes])
    for remain_pile in range(2, piles+1):
        minimum = least
        repile(minimum, remain_pile, dishes, every_case)

    possible = 0
    for line in every_case:
        unique = set(line)
        repeat = [line.count(each) for each in unique] # optimiz: if count > 1
        div = product([factorial(each) for each in repeat+line])
        possible += Fraction(factorial(dishes), div)
        # print(repeat, line, div, possible)

    print(possible % 9871)

