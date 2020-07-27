#!/usr/bin/env python3


def flight_table(n, incoming, outgoing):
    table = [[i == j for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if outgoing[j-1] == 'Y' and incoming[j] == 'Y':
                table[i][j] = True
            else:
                break
        for j in reversed(range(i)):
            if outgoing[j+1] == 'Y' and incoming[j] == 'Y':
                table[i][j] = True
            else:
                break
    return table


def main():
    for c in range(int(input())):
        n = int(input())
        incoming = input().strip()
        outgoing = input().strip()
        table = flight_table(n, incoming, outgoing)
        print(f'Case #{c+1}:')
        for line in table:
            print(''.join('Y' if x else 'N' for x in line))


if __name__ == '__main__':
    main()
