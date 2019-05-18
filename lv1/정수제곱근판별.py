import math

def solution(n):
    x = math.sqrt(n)
    if math.ceil(x) == x:
        return (x + 1) ** 2
    return -1

def solution2(n):
    x = n ** .5
    if x % 1 == 0:
        return (x + 1) ** 2
    return -1

def solution3(n):
    x = n ** .5
    return -1 if x % 1 > 0 else (x + 1) ** 2
