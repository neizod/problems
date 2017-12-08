#!/usr/bin/env python3


def arrive_time(dest, init, speed):
    return (dest-init) / speed


def cruise_speed(dest, horses):
    return dest / max(arrive_time(dest, *horse) for horse in horses)


def main():
    for case in range(int(input())):
        dest, n_horses = [int(n) for n in input().split()]
        horses = [tuple(int(n) for n in input().split()) for _ in range(n_horses)]
        print('Case #{}: {}'.format(case+1, cruise_speed(dest, horses)))


if __name__ == '__main__':
    main()
