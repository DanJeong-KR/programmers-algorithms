def solution(name):
    answer = 0
    num = list(map(lambda x:min(ord(x) - ord('A'), ord('Z') + 1 - ord(x)), name))
    index = 0
    while sum(num) > 0:
        answer += num[index]
        num[index] = 0

        if sum(num) == 0:
            break

        right = index
        rightDist = 0
        for c in range(len(num)-1): # 오른쪽
            right += 1
            rightDist += 1
            if right == len(num):
                right = 0
            if num[right] > 0:
                break

        left = index
        leftDist = 0
        for c in range(len(num)-1): # 왼쪽
            left -= 1
            leftDist += 1
            if left == -1:
                left = len(num) - 1
            if num[left] > 0:
                break

        if rightDist > leftDist:
            index = left
            answer += leftDist
        else:
            index = right
            answer += rightDist



    return answer
