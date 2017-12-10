#!/usr/bin/env python3


def check(regs, n, comp, value):
    if comp == '>':
        return regs[n] > value
    if comp == '<':
        return regs[n] < value
    if comp == '>=':
        return regs[n] >= value
    if comp == '<=':
        return regs[n] <= value
    if comp == '!=':
        return regs[n] != value
    if comp == '==':
        return regs[n] == value
    raise KeyError('comparator {} not exists!'.format(comp))


def update(regs, n, opt, value):
    if opt == 'inc':
        regs[n] += value
    elif opt == 'dec':
        regs[n] -= value
    else:
        raise KeyError('operation {} not exists!'.format(opt))


def main():
    regs = {}
    try:
        largest = 0
        while True:
            ir, opt, iv, _, cr, comp, cv = input().split()
            iv, cv = [int(n) for n in [iv, cv]]
            if ir not in regs:
                regs[ir] = 0
            if cr not in regs:
                regs[cr] = 0
            if check(regs, cr, comp, cv):
                update(regs, ir, opt, iv)
                largest = max(largest, regs[ir])
    except EOFError:
        print(largest)


if __name__ == '__main__':
    main()
