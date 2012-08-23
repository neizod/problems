def minimum(col, curr, prev):
    if col == 0:
        plus = min([prev[col], prev[col+1]])
    elif col == cols-1:
        plus = min([prev[col-1], prev[col]])
    else:
        plus = min([prev[col-1], prev[col], prev[col+1]])

    return curr[col] + plus


for test in range(int(input())):
    rows, cols = [int(num) for num in input().split()]

    for row in range(rows):
        if row == 0:
            earth = [int(num) for num in input().split()]
            continue

        prev = earth[:]
        curr = [int(num) for num in input().split()]
        earth = [minimum(col, curr, prev) for col in range(cols)]

    print(min(earth))

