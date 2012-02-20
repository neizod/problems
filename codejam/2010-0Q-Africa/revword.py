# one line version:
# print('\n'.join('Case #{}: {}'.format(test+1, ' '.join(word for word in input().split()[::-1])) for test in range(int(input()))))

for test in range(int(input())):
    revword = ' '.join(word for word in input().split()[::-1])
    print('Case #{}: {}'.format(test+1, revword))
