from functools import reduce

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = []

    while len(truck_weights) > 0 or len(bridge) > 0:
        answer += 1 # 경과 시간 +1
        bridge = list(map(lambda x: [x[0], x[1]+1], bridge)) # 트럭 시간 +1
        bridge = list(filter(lambda x: x[1] <= bridge_length, bridge)) # 통과한 트럭 제거

        # 트럭 추가
        if len(truck_weights) > 0: # 남은 트럭이 있으면
            # 다리 위의 트럭 무게 합 + 남은 트럭 1개 무게 <= 가능한 무게
            if (reduce(lambda x, y: x + y[0], bridge, 0) + truck_weights[0]) <= weight:
                bridge.append([truck_weights.pop(0), 1]) # 트럭 추가

    return answer
