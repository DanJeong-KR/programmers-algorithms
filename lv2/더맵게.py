import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 리스트 -> 우선순위 큐

    while len(scoville) > 1: # 원소가 2 이상
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville) * 2
        heapq.heappush(scoville, a+b)

        answer += 1 # 횟수 +1
        if scoville[0] >= K: # 우선순위 큐의 min만 검사
            return answer

    return -1
