from itertools import permutations

def find_match(credit, size, price):
    for x, y in permutations(range(size), 2):
        if price[x] + price[y] == credit:
            return x+1, y+1

def test(case):
    credit = int(input())
    size = int(input())
    price = [int(n) for n in input().split()]
    return find_match(credit, size, price)

def main():
    for case in range(int(input())):
        x, y = test(case)
        print('Case #{}: {} {}'.format(case+1, x, y))

if __name__ == '__main__':
    main()

