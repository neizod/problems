def recycle(m, r):
    global pair, count
    if r > 0:
        m = m%digit * 10 + m//digit
        if lower <= n < m <= upper and m not in pair.setdefault(n, []):
            pair[n].append(m)
            count += 1
        recycle(m, r-1)

for test in range(int(input())):
    lower, upper = [int(n) for n in input().split()]
    round = len(str(lower)) - 1
    digit = 10 ** round

    pair = {}
    count = 0
    for n in range(lower, upper+1):
        recycle(n, round)

    print('Case #{}: {}'.format(test+1, count))
