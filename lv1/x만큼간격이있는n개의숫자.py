def solution(x, n):
    answer = []
    val = 0
    for i in range(n):
        val += x
        answer.append(val)
    return answer

def solution2(x, n):
    return [x + x * i for i in range(n)]
