#!/usr/bin/env python3


def solve(months, down, price, table):
    pay = price / months
    remain = price + pay
    price += down
    for i in range(months+1):
        if i in table:
            rate = table[i]
        remain -= pay
        price *= 1 - rate
        if remain < price:
            return i
    return i


def main():
    try:
        while True:
            table = {}
            months, down, price, depricate = input().split()
            months = int(months)
            down = float(down)
            price = float(price)
            depricate = int(depricate)
            for _ in range(depricate):
                i, rate = input().split()
                i = int(i)
                rate = float(rate)
                table[i] = rate
            i = solve(months, down, price, table)
            m = 'month' if i == 1 else 'months'
            print(f'{i} {m}')
    except EOFError:
        pass


if __name__ == '__main__':
    main()
