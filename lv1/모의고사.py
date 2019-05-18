def solution(answers):
    answer = []

    score = [0, 0, 0]

    pattern = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]

    for n, c in enumerate(answers):
        if c == pattern[0][n % 5]:
            score[0] += 1
        if c == pattern[1][n % 8]:
            score[1] += 1
        if c == pattern[2][n % 10]:
            score[2] += 1

    for n, c in enumerate(score):
        if c == max(score):
            answer.append(n+1)

    return answer
