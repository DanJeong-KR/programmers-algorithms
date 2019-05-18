# 문자열 함수 사용
def solution(s):
    return (len(s) == 4 or len(s) == 6) and s.isdigit()
    return len(s) in (4, 6) and s.isdigit()
