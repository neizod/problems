for case in range(int(input())):
    size = int(input())

    a = sorted(int(val) for val in input().split())
    b = sorted(int(val) for val in input().split())[::-1]

    scalar = sum(a[i]*b[i] for i in range(size))

    print('Case #{}: {}'.format(case+1, scalar))

