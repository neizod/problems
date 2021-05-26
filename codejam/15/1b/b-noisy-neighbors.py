#!/usr/bin/env python3


is_odd = lambda n: n % 2 == 1


def extract_info(table):
    rows = len(table)
    cols = len(table[0])
    full = rows * cols
    emp = sum(v for line in table for v in line)
    cor = table[0][0] + table[0][-1] + table[-1][0] + table[-1][-1]
    inn = sum(v for r, line in enumerate(table)
                for c, v in enumerate(line)
                if 0 < c < cols-1 and 0 < r < rows-1)
    if rows == 1:
        inn = sum(v for c, v in enumerate(table[0]) if 0 < c < cols-1)
        return (full-emp), (emp-inn), inn, 0, 0
    return (full-emp), 0, cor, (emp-inn-cor), inn


def unhappiness(n, info):
    unhappy_point = 0
    for weight, avail in enumerate(info):
        unhappy_point += weight * min(n, avail)
        n -= min(n, avail)
        if n == 0:
            break
    return unhappy_point


def solve(rows, cols, n):
    rows, cols = sorted([rows, cols])
    table_1 = [[is_odd(r)^is_odd(c) for c in range(cols)] for r in range(rows)]
    info_1 = extract_info(table_1)
    if is_odd(rows) and is_odd(cols):
        table_2 = [[not v for v in line] for line in table_1]
        info_2 = extract_info(table_2)
    else:
        info_2 = info_1
    answer = min(unhappiness(n, info_1), unhappiness(n, info_2))
    return answer


def main():
    for case in range(int(input())):
        rows, cols, n = [int(x) for x in input().split()]
        print(f'Case #{case+1}: {solve(rows, cols, n)}')


if __name__ == '__main__':
    main()
