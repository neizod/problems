#!/usr/bin/env python3


def clear_tail(i, ls, memo):
    while ls[memo[i]][-1] != i:
        x = ls[memo[i]].pop()
        ls[x] += [x]
        memo[x] = x


def just_move(a, b, ls, memo):
    index = ls[memo[a]].index(a)
    ls[memo[a]], moving = ls[memo[a]][:index], ls[memo[a]][index:]
    ls[memo[b]] += moving
    for x in moving:
        memo[x] = memo[b]


def robot(ma, mb, a, b, ls, memo):
    if a == b or memo[a] == memo[b]:
        return
    if ma == 'move':
        clear_tail(a, ls, memo)
    if mb == 'onto':
        clear_tail(b, ls, memo)
    just_move(a, b, ls, memo)


def main():
    ls = {i: [i] for i in range(int(input()))}
    memo = {i: i for i in ls}
    while True:
        cmd = input()
        if cmd == 'quit':
            break
        ma, ra, mb, rb = cmd.split()
        robot(ma, mb, int(ra), int(rb), ls, memo)
    for key, value in sorted(ls.items()):
        print('{}:'.format(key), end='')
        for v in value:
            print(' {}'.format(v), end='')
        print()


if __name__ == '__main__':
    main()
