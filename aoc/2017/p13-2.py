#!/usr/bin/env python3


def go(firewall):
    cycle = [(scan-1)*2 for scan in firewall]
    delay = 0
    while any((c+i+delay)%c == 0 for i, c in zip(range(len(firewall)), cycle)):
        print(delay)
        delay += 1
    return delay


def main():
    try:
        firewall = []
        while True:
            layer, height = [int(n) for n in input().split(': ')]
            while len(firewall) < layer:
                firewall += [1e400]
            firewall += [height]
    except EOFError:
        print(go(firewall))


if __name__ == '__main__':
    main()
