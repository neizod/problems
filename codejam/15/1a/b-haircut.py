#!/usr/bin/env python3

class Barbershop(object):
    def do_haircut(self):
        m = min(self.barbers)
        if m > 0:
            self.barbers = [b - m for b in self.barbers]
        available_index = self.barbers.index(0)
        self.barbers[available_index] = self.speed[available_index]
        return available_index

    def __init__(self, speed, time=0):
        self.speed = speed
        self.barbers = [time % s for s in self.speed]


def div_ceil(a, b):
    return a//b + (a%b > 0)


def reduce_waiting_queue(n, ms):
    lower = 0
    upper = n * min(ms)
    while upper - lower > 1:
        middle = (lower + upper) // 2
        customer = sum(div_ceil(middle, m) for m in ms)
        if customer < n:
            lower = middle
        else:
            upper = middle
    customer = sum(div_ceil(lower, m) for m in ms)
    barbers = Barbershop(ms, lower)
    return n-1-customer, barbers


def get_barber(n, ms):
    n, barbers = reduce_waiting_queue(n, ms)
    while n:
        barbers.do_haircut()
        n -= 1
    return 1 + barbers.do_haircut()


for case in range(int(input())):
    _, n = [int(i) for i in input().split()]
    ms = [int(i) for i in input().split()]
    ans = get_barber(n, ms)
    print('Case #{}: {}'.format(case+1, ans))
