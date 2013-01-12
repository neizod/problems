for case in range(int(input())):
    revword = ' '.join(word for word in input().split()[::-1])
    print('Case #{}: {}'.format(case+1, revword))

