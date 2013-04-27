def sqrt(n):
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2 ** (a + b)
    while True:
        y = x + n // x
        y //= 2
        if y >= x:
            return x
        x = y

def find_it(r, t):
    pr = 2 * r - 1
    rt = sqrt(pr**2 + 8 * t)
    a1 = -pr + rt
    a2 = -pr - rt
    return (a1 if a1 > 0 else a2) // 4

for case in range(int(input())):
    r, t = [int(n) for n in input().split()]
    answer = find_it(r, t)
    print('Case #{}: {}'.format(case+1, answer))
