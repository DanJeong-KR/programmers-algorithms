def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)

def lcm(a, b):
    return a * b / gcd(a, b)

def solution(n, m):
    return [gcd(n, m), lcm(n, m)]
