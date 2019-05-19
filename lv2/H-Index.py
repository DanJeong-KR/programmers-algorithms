def solution(citations):
    answer = 0
    citations.sort()
    for i in range(0, len(citations)+1):
        count = 0
        for c in citations:
            if c >= i:
                count += 1
        if count >= i:
            answer = i
    return answer
