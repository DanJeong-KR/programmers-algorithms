# return 함수 사용법
def solution(arr, divisor):
    answer = sorted([n for n in arr if n % divisor == 0])
    return [-1] if len(answer) == 0 else answer
