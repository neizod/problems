def foo(answer_1, matrix_1, answer_2, matrix_2):
    candidate_1 = matrix_1[answer_1-1]
    candidate_2 = matrix_2[answer_2-1]
    final = set(candidate_1) & set(candidate_2)
    if len(final) == 0:
        return 'Volunteer cheated!'
    elif len(final) > 1:
        return 'Bad magician!'
    else:
        return final.pop()


for case in range(int(input())):
    answer_1 = int(input())
    matrix_1 = [[int(n) for n in input().split()] for _ in range(4)]
    answer_2 = int(input())
    matrix_2 = [[int(n) for n in input().split()] for _ in range(4)]
    answer = foo(answer_1, matrix_1, answer_2, matrix_2)
    print('Case #{}: {}'.format(case+1, answer))
