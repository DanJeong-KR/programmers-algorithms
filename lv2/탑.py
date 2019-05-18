def solution(heights):
    answer = []
    record = [] # [[번호, 높이], ...]
    for i, h in enumerate(heights):
        for j in reversed(range(len(record))): # 스택 뒤에서 탐색
            if record[j][1] <= h: # 현재 탑보다 작다면
                record.pop() # 스택에서 제거
            else: # 현재 탑보다 크다면
                answer.append(record[j][0]+1) # 큰 탑의 인덱스 저장
                break
        else:
            answer.append(0) # 큰 탑이 없을 때
        record.append([i, h]) # 현재 탑 저장
    return answer
