from functools import cmp_to_key

# 문자열로 합친 뒤에 숫자로 비교
def compare(a, b):
    if int(a + b) > int(b + a):
        return -1
    elif int(a + b) < int(b + a):
        return 1
    else:
        return 0

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=cmp_to_key(compare))
    answer = str(int(''.join(numbers))) # '000001234'일 경우 처리
    return answer
