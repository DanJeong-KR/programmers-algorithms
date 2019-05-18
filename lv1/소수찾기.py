def solution(n):
    answer = 0
    isPrime = [False, False] + [True] * n # 소수 후보군. 0, 1은 제외
    for i in range(2, n+1): # 2부터 시작
        if isPrime[i]:
            answer += 1 # 소수 찾기
            for j in range(i*i, n+1, i): # 찾은 소수의 배수는 제거
                isPrime[j] = False # 소수 후보에서 제외
    return answer
