def solution(n):
    answer = n

    for i in range(1, n+1//2): # 반만 검사
        if n % i == 0:
            answer += i

    return answer
