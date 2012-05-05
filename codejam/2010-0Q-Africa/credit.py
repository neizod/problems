# one-liner version
'\n'.join('Case #{}: {} {}'.format(test+1, *[i[0]+1 for c in (lambda x, y: (x,))(int(input()), int(input())) for i, l in (lambda x: zip(enumerate(e for e in x), [x for e in x]))([int(v) for v in input().split()]) for j in enumerate(l) if i[1] + j[1] == c and i[0] != j[0]]) for test in range(int(input()))))

###############################################################################


﻿def find_match(credit, size, price):
    for x in range(size-1):
        for y in range(x+1, size):
            if price[x] + price[y] == credit:
                return x, y


for i in range(int(input())):
    credit = int(input())
    size = int(input())
    price = [int(val) for val in input().split()]

    x, y = find_match(credit, size, price)
    print('Case #{}: {} {}'.format(i+1, x+1, y+1))
