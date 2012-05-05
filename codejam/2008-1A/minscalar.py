# one-liner version
"\n".join("Case #{0}: {2}".format(test+1, input(), sum(a*b for a, b in zip(sorted(int(val) for val in input().split()), sorted(int(val) for val in input().split())[::-1]))) for test in range(int(input())))

###############################################################################


for test in range(int(input())):
    size = int(input())

    a = sorted(int(val) for val in input().split())
    b = sorted(int(val) for val in input().split())[::-1]

    scalar = sum(a[i]*b[i] for i in range(size))

    print("Case #{}: {}".format(test+1, scalar))
