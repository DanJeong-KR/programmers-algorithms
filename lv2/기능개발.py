import math

def solution(progresses, speeds):
    answer = []
    big = 0 # 스택 탑

    for p, s in zip(progresses, speeds):
        day = math.ceil((100 - p) / s) # 배포 가능 날

        if big < day: # 작업 추가
            answer.append(1)
            big = day
        else: # 앞 작업이 더 오래 걸릴 때
            answer[-1] += 1

    return answer
