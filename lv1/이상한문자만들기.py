def solution(s):
    s = s.split(' ') # 문자열 -> 리스트(단어, 단어, 단어)
    answer = []
    for word in s: # 단어마다
        x = '' # 새로운 단어
        for n, c in enumerate(word):
            if n % 2 == 0:
                x += word[n].upper()
            else:
                x += word[n].lower()
        answer.append(x) # 단어 리스트에 추가
    return ' '.join(answer)
