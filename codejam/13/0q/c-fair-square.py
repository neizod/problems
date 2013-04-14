odd = lambda x: x % 2 == 1
square = lambda n: int(n ** 0.5) ** 2 == n
palindrome = lambda n: str(n) == str(n)[::-1]

def int_sqrt(n):
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

def next_palindrome(n):
    s = str(n)
    size = len(s)

    fst = s[:size//2+1] if odd(size) else s[:size//2]
    lst = s[-size//2:]

    size_old_fst = len(fst)
    if fst <= lst[::-1]:
        fst = str(int(fst) + 1)

    lst = fst[:-1] if len(fst) > size_old_fst else fst
    return int(fst[:-1] + lst[::-1]) if odd(size) else int(fst + lst[::-1])

def palindrome_range(start, stop):
    while start < stop:
        if palindrome(start):
            yield start
        start = next_palindrome(start)

for case in range(int(input())):
    start, stop = [int(n) for n in input().split()]

    start = int_sqrt(start) + (0 if square(start) else 1)
    stop = int_sqrt(stop)

    answer = sum(palindrome(pal**2) for pal in palindrome_range(start, stop+1))
    print('Case #{}: {}'.format(case+1, answer))
