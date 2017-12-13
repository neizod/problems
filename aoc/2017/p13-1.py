#!/usr/bin/env python3


def go(firewall):
    cycle = [(scan-1)*2 for scan in firewall]
    caught = [(c+i)%c for i, c in zip(range(len(firewall)), cycle)]
    return sum(i*firewall[i] for i, v in enumerate(caught) if v == 0)


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
