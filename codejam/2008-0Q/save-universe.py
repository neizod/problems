for test in range(int(input())):
    name = {input() for _ in range(int(input()))}

    result = 0
    used = name.copy()
    for _ in range(int(input())):
        query = input()
        used -= {query}
        if not used:
            used = name.copy() - {query}
            result += 1

    print('Case #{}: {}'.format(test+1, result))

