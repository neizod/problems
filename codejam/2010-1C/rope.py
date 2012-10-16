for test in range(int(input())):
    wired = {}
    for connect in range(int(input())):
        k, v = [int(val) for val in input().split()]
        wired[k] = v

    order = [wired[k] for k in sorted(wired)]

    intersect = 0
    while len(order):
        moveit = min(order)
        remove = order.index(moveit)
        order.pop(remove)
        intersect += remove

    print('Case #{}: {}'.format(test+1, intersect))
