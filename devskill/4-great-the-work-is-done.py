#!/usr/bin/env python3

def main():
    try:
        while True:
            hours, n = [int(n) for n in input().split()]
            perf = sum(int(input()) for _ in range(n))
            days, rem = divmod(hours, perf)
            days += (rem > 0)
            if days == 1:
                print('Project will finish within {} day.'.format(days))
            else:
                print('Project will finish within {} days.'.format(days))
    except EOFError:
        pass


if __name__ == '__main__':
    main()
