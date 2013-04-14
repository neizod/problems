def transpose(lawn):
    return [list(line) for line in zip(*lawn)]

def beautiful_garden(lawn, n, m):
    tlawn = transpose(lawn)
    def chk(y, x):
        return lawn[y][x] in [max(tlawn[x]), max(lawn[y])]
    return all(all(chk(y, x) for x in range(m)) for y in range(n))

for case in range(int(input())):
    n, m = [int(i) for i in input().split()]
    lawn = [[int(i) for i in input().split()] for _ in range(n)]
    answer = 'YES' if beautiful_garden(lawn, n, m) else 'NO'
    print('Case #{}: {}'.format(case+1, answer))
