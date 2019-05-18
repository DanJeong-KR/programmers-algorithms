def solution(n, lost, reserve):
    answer = 0
    suits = [1 for i in range(n)] # [1] * n

    for i in lost:
        suits[i-1] -= 1

    for i in reserve:
        suits[i-1] += 1

    for i, suit in enumerate(suits):
        if suit == 0:
            if i == 0 and suits[i+1] < 2:
                continue
            elif i == n-1 and suits[i-1] < 2:
                continue
            elif suits[i-1] > 0:
                answer += 1
            elif suits[i+1] == 2:
                answer += 1
                suits[i+1] -= 1
        else:
            answer += 1
            suits[i] -= 1

    return answer
