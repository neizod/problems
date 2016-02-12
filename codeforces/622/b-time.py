#!/usr/bin/env python3


def time_after(hours, minutes, add_minutes):
    minutes += add_minutes
    add_hours, minutes = divmod(minutes, 60)
    hours += add_hours
    hours %= 24
    return hours, minutes


def main():
    hours, minutes = [int(n) for n in input().split(':')]
    add_minutes = int(input())
    print('{:02}:{:02}'.format(*time_after(hours, minutes, add_minutes)))


if __name__ == '__main__':
    main()
