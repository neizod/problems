def transpose(grid):
    return [''.join(line) for line in zip(*grid)]

def chk_hori(grid):
    for line in grid:
        if all(c in 'XT' for c in line):
            return 'X won'
        if all(c in 'OT' for c in line):
            return 'O won'

def chk_diag(grid):
    if all(grid[i][i] in 'XT' for i in range(len(grid))):
        return 'X won'
    if all(grid[i][i] in 'OT' for i in range(len(grid))):
        return 'O won'

def chk_won(grid):
    for _ in range(2):
        for chk in [chk_hori, chk_diag]:
            answer = chk(grid)
            if answer:
                return answer
        grid = transpose(reversed(grid))

def chk_full(grid):
    return not any('.' in line for line in grid)

for case in range(int(input())):
    grid = [input() for _ in range(4)]
    input()
    answer = chk_won(grid)
    if not answer:
        answer = 'Draw' if chk_full(grid) else 'Game has not completed'
    print('Case #{}: {}'.format(case+1, answer))
