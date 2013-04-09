for case in range(int(input())):
    depth, keys, _ = [int(n) for n in input().split()]
    frequency = sorted(int(n) for n in input().split())[::-1]

    layout = [frequency[d*keys:(d+1)*keys] for d in range(depth)]
    total = sum(d * sum(layer) for d, layer in enumerate(layout, 1))

    print('Case #{}: {}'.format(case+1, total))

