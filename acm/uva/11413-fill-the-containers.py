#!/usr/bin/env python3

def bin_search_target(ls, m):
    lower = max(ls)
    upper = sum(ls)
    while upper != lower:
        now = (upper + lower) // 2
        if m >= n_container(now, ls):
            upper = now
        else:
            lower = now + 1
    return upper


def n_container(target, ls):
    ls = ls[:]
    val = 0
    use = 0
    while ls:
        if val == 0:
            use += 1
        get = ls.pop()
        val += get
        if val > target:
            ls.append(get)
        if val >= target:
            val = 0
    return use


def main():
    try:
        while True:
            _, m = [int(n) for n in input().split()]
            ls = [int(n) for n in input().split()]
            print(bin_search_target(ls, m))
    except EOFError:
        pass


if __name__ == '__main__':
    main()
