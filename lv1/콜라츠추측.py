def solution(num):
    count = -1
    while count < 500:
        count += 1
        if num == 1:
            return count
        elif num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
    return -1
