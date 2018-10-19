#!/usr/bin/env python3


def parse(string):
    chessboard = [['' for _ in range(8)] for _ in range(8)]
    for i, line in enumerate(string.split('/')):
        j = 0
        for ch in line:
            if ch.isdigit():
                j += int(ch)
            else:
                chessboard[i][j] = ch
                j += 1
    return chessboard


def mark(y, x, result):
    if 0 <= y < 8 and 0 <= x < 8:
        result[y][x] = 0
        return True
    return False


def fill(i, j, chessboard, result):
    piece = chessboard[i][j]
    mark(i, j, result)
    if piece.lower() == 'p':
        dy = 1 if piece == 'p' else -1
        for dx in [-1, +1]:
            mark(i+dy, j+dx, result)
    if piece.lower() == 'n':
        for da, db in [(+1,+2), (+1,-2), (-1,+2), (-1,-2)]:
            for _ in range(2):
                da, db = db, da
                y, x = i+da, j+db
                mark(y, x, result)
    if piece.lower() == 'k':
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                y, x = i+dy, j+dx
                mark(y, x, result)
    if piece.lower() in 'rq':
        for a, b in [(+1, 0), (-1, 0), (0, +1), (0, -1)]:
            for dd in range(1, 8):
                y, x = i+a*dd, j+b*dd
                if not mark(y, x, result) or chessboard[y][x]:
                    break
    if piece.lower() in 'bq':
        for a, b in [(+1,+1), (+1,-1), (-1,+1), (-1,-1)]:
            for dd in range(1, 8):
                y, x = i+a*dd, j+b*dd
                if not mark(y, x, result) or chessboard[y][x]:
                    break


def threaten(chessboard):
    result = [[1 for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            if not chessboard[i][j]:
                continue
            fill(i, j, chessboard, result)
    return result


def main():
    try:
        while True:
            chessboard = parse(input())
            result = threaten(chessboard)
            print(sum(sum(line) for line in result))
    except EOFError:
        pass


if __name__ == '__main__':
    main()
