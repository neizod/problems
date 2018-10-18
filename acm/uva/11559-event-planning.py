#!/usr/bin/env python3


def main():
    try:
        while True:
            people, budget, hotels, _ = [int(n) for n in input().split()]
            cost = 1e400
            for _ in range(hotels):
                price = int(input())
                avail = [int(n) for n in input().split()]
                if price * people > budget or max(avail) < people:
                    continue
                cost = min(cost, price * people)
            print('stay home' if cost == 1e400 else cost)
    except EOFError:
        pass


if __name__ == '__main__':
    main()
