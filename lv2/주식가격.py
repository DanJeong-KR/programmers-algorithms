def solution(prices):
    answer = []

    for i in range(len(prices)): # 첫번째 루프
        count = 0 # 기본값
        for val in range(i+1, len(prices)): # 두번째 루프
            count += 1 # 루프가 남아있으면 +1
            if prices[i] > prices[val]: # 자신보다 작으면 break
                break
        answer.append(count) # 리스트 추가

    return answer
