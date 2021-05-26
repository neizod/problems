#!/usr/bin/env python3

def solve(q, students):
    best_score = 0
    best_answer = ''
    for score, answer in students:
        answer = [a == 'T' for a in answer]
        if score < q/2:
            answer = [not a for a in answer]
            score = q - score
        if score > best_score:
            best_score = score
            best_answer = answer
    return best_score, ''.join('FT'[a] for a in best_answer)


def main():
    for case in range(int(input())):
        n, q = [int(x) for x in input().split()]
        students = []
        for _ in range(n):
            raw = input().split()
            students += [(int(raw[1]), raw[0])]
        expect, answer = solve(q, students)
        print(f'Case #{case+1}: {answer} {expect}/1')


if __name__ == '__main__':
    main()
