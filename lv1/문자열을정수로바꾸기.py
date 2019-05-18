# 쉬운 방법
def solution(s):
    return int(s)

# 정공법
def solution2(s):
    answer = 0
    sign = 1
    for num in s:
        if num == '+':
            sign = 1
        elif num == '-':
            sign = -1
        else:
            answer = answer * 10 + ord(num) - ord('0') # 문자열 -> 아스키 코드
    return sign * answer
