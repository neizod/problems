while True:
    try:
        n, *r = [int(e) for e in input().split()]

        # find diff from input sequence.
        s = [abs(i-j) for i, j in zip(r[:-1], r[1:])]

        # create list of integet for comparasion [1, 2, 3, ..., n]
        c = list(range(1, n))

        if c == sorted(s):
            print('Jolly')
        else:
            print('Not jolly')

    except EOFError:
        break
