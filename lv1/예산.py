def solution(d, budget):
    answer = 0
    for x in sorted(d):
        if budget >= x:
            budget -= x
            answer += 1
    return answer
