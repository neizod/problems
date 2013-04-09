from itertools import combinations
from functools import reduce
from fractions import gcd

lcm = lambda a, b: a * b // gcd(a, b)
odd = lambda n: n % 2 == 1   

def count_slap(set_dragons, nos_dragons, total=0):
    for how_many, dragon in enumerate(set_dragons, 1):
        for group in combinations(set_dragons, how_many):
            if odd(how_many):
                total += nos_dragons // reduce(lcm, group)
            else:
                total -= nos_dragons // reduce(lcm, group)
    return total

def main():
    k, l, m, n, d = [int(input()) for _ in range(5)]
    print(count_slap({k, l, m, n}, d))

if __name__ == '__main__':
    main()
