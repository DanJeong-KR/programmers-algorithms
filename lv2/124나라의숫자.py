def solution(n):
    answer = ''
    num = '412' # 3진법: 012

    while n > 0:
        i = n % 3
        n //= 3
        if i == 0: # 나머지가 0일 때
            n -= 1 # 1을 빼야 3 배수는 자리수가 올라가지 않는다
        answer = num[i] + answer

    return answer
