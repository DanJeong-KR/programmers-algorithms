def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    low = 0
    high = len(people) - 1
    while low <= high:
        if people[low] + people[high] <= limit:
            high -= 1
        answer += 1
        low += 1

    return answer
