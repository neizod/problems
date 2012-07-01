exit('JOLLY!' if list(range(1, int(input()))) == (lambda r: sorted([abs(i-j) for i, j in zip(r[:-1], r[1:])]))([int(n) for n in input().split()]) else 'NOT JOLLY!')


n = int(input())
r = [int(e) for e in input().split()]

c = list(range(1, n))
s = [abs(i-j) for i, j in zip(r[:-1], r[1:])]

if c == sorted(s):
    print('JOLLY!')
else:
    print('NOT JOLLY!')
