for case in range(int(input())):
    wired = {}
    for connect in range(int(input())):
        k, v = [int(val) for val in input().split()]
        wired[k] = v

    order = [v for k, v in sorted(wired.items())]

    intersect = 0
    while order:
        moveit = min(order)
        remove = order.index(moveit)
        order.pop(remove)
        intersect += remove

    print('Case #{}: {}'.format(case+1, intersect))

