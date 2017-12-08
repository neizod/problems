#!/usr/bin/env python3

import re

def ev(expr):
    if expr[1] == '+':
        return [expr[0] + expr[2]]
    return [expr[0] * expr[2]]

def kill(expr, symbol):
    while True:
        try:
            index = expr.index(symbol)
            expr = expr[:index-1] + ev(expr[index-1:index+2]) + expr[index+2:]
        except ValueError:
            return expr

def maximum(expr):
    expr = kill(expr, '+')
    expr = kill(expr, '*')
    return expr[0]

def minimum(expr):
    expr = kill(expr, '*')
    expr = kill(expr, '+')
    return expr[0]

for _ in range (int(input ())):
    expr = [int(x) if x.isdigit() else x for x in re.split(r'(\+|\*)', input())]
    print('The maximum and minimum are {} and {}.'.format(maximum(expr), minimum(expr)))
