exit('\n'.join('Case #{}: {}'.format(test+1, ' '.join(word for word in input().split()[::-1])) for test in range(int(input()))))
