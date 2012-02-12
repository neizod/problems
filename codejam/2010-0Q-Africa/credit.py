def find_match(credit, size, price):
    for x in range(size-1):
        for y in range(x+1, size):
            if price[x] + price[y] == credit:
                return x, y

################################################################################

for i in range(int(input())):
    credit = int(input())
    size = int(input())
    price = [int(val) for val in input().split()]

    x, y = find_match(credit, size, price)
    print('Case #{}: {} {}'.format(i+1, x+1, y+1))
