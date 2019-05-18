import math

# 수학적
def solution2(n):
    s = '수박' * math.ceil(n/2)
    return s[:n]

# 쉬운 방법
def solution2(n):
    s = ''
    for i in range(1, n+1):
        if i % 2 == 1:
            s += '수'
        else:
            s += '박'
    return s
