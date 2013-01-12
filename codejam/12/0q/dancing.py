from math import ceil

for case in range(int(input())):
    gg, surprise, expected, *point = [int(n) for n in input().split()]
    point.sort(reverse=True)

    count = 0
    for p in point:
        if ceil(p/3) >= expected:
            count += 1
        elif surprise > 0 and ceil(p/3)+1 >= expected:
            if p%3 == 1 or p in (0, 1):
                continue
            count += 1
            surprise -= 1

    print('Case #{}: {}'.format(case+1, count))
