# 아스키 코드
# 대문자 알파벳 아스키 코드 < 소문자 알파벳 아스키 코드
def solution(s, n):
    answer = ''
    for c in s:
        if c == ' ':
            answer += c
        elif c >= 'a':
            answer += chr((ord(c) - ord('a') + n) % 26 + ord('a'))
        elif c:
            answer += chr((ord(c) - ord('A') + n) % 26 + ord('A'))
    return answer
