#!/usr/bin/env python3


def snail(h, u, d, f):
    day = 1
    pos = 0
    loss = f * u / 100
    while True:
        pos += u
        if pos > h:
            return day, True
        pos -= d
        if pos < 0:
            return day, False
        u = max(0, u-loss)
        day += 1


def main():
    while True:
        h, u, d, f = [int(n) for n in input().split()]
        if h == 0:
            break
        day, done = snail(h, u, d, f)
        report = 'success' if done else 'failure'
        print('{} on day {}'.format(report, day))
    pass


if __name__ == '__main__':
    main()
