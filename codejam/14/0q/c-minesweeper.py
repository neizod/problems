def transpose(matrix):
    return [list(line) for line in zip(*matrix)]

def fill_line(r, c, left):
    width, length = sorted([r, c])
    matrix = [['*' for _ in range(length)] for _ in range(width)]
    for i in range(width):
        matrix[i][:left//width] = ['.' for _ in range(left//width)]
    matrix[0][0] = 'c'
    return matrix if r == len(matrix) else transpose(matrix)

def fill_rect(r, c, left):
    width, length = sorted([r, c])
    sq_length = int(left**0.5)
    matrix = [['*' for _ in range(width)] for _ in range(length)]
    if sq_length > width:
        i = 0
        while left - width > 0:
            matrix[i] = ['.' for _ in range(width)]
            left -= width
            i += 1
        if left == 1:
            matrix[i-1][-1:] = ['*']
            matrix[i][:2] = ['.' for _ in range(2)]
        else:
            matrix[i][:left] = ['.' for _ in range(left)]
    else:
        i = 0
        while i < sq_length:
            matrix[i][:sq_length] = ['.' for _ in range(sq_length)]
            left -= sq_length
            i += 1
        if left > sq_length:
            if left == sq_length + 1:
                matrix[i][:sq_length-1] = ['.' for _ in range(sq_length-1)]
                left = 2
            else:
                matrix[i][:sq_length] = ['.' for _ in range(sq_length)]
                left -= sq_length
            if i == len(matrix)-1:
                matrix = transpose(matrix)
            else:
                i += 1
            matrix[i][:left] = ['.' for _ in range(left)]
        elif left > 0:
            if left == 1:
                matrix[i-1][sq_length-1:sq_length] = ['*']
                left = 2
            matrix[i][:left] = ['.' for _ in range(left)]
    matrix[0][0] = 'c'
    return matrix if r == len(matrix) else transpose(matrix)

def mine_fill(r, c, m):
    width = min(r, c)
    left = r * c - m
    if width == 1:
        if left == 0:
            return None
        return fill_line(r, c, left)
    if width == 2:
        if left in [0, 2] or left % 2 == 1 and left != 1:
            return None
        return fill_line(r, c, left)
    else:
        if left in [0, 2, 3, 5, 7]:
            return None
        return fill_rect(r, c, left)

for case in range(int(input())):
    r, c, m = [int(n) for n in input().split()]
    answer = mine_fill(r, c, m)
    print('Case #{}:'.format(case+1))
    if answer is None:
        print('Impossible')
    else:
        for line in answer:
            print(''.join(line))
