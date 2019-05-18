def solution(n, lost, reserve):
    answer = 0

    # 초기 설정

    # 모든 학생에게 기본으로 1벌씩
    suits = [1 for i in range(n)] # [1] * n

    for i in lost: # 잃어버린 학생
        suits[i-1] -= 1

    for i in reserve: # 여벌있는 학생
        suits[i-1] += 1

    for i, suit in enumerate(suits):
        if suit == 0: # 옷이 없으면 옆 친구에게 빌린다
            if i == 0 and suits[i+1] < 2:
                continue # 1번, 2번 모두 옷이 부족하다
            elif i == n-1 and suits[i-1] < 2:
                continue # 마지막과 마지막 앞 학생 모두 옷이 부족하다
            elif suits[i-1] > 0: # 앞 학생에게 빌린다
                answer += 1
            elif suits[i+1] == 2: # 뒤 학생에게 빌린다
                answer += 1
                suits[i+1] -= 1
        else: # 자기 옷을 입는다
            answer += 1
            suits[i] -= 1

    return answer
