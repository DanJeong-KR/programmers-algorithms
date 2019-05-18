def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        remain = list(skill)
        for leaf in tree:
            if leaf in remain:
                if leaf != remain.pop(0):
                    break
        else: # for문 안에서 break 안 만난다면 실행
            answer += 1
    return answer

def solution2(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        remain = list(skill)[::-1]
        isPossible = True
        for leaf in tree:
            if leaf in remain:
                if leaf == remain[-1]:
                    remain.pop()
                else:
                    isPossible = False
                    break
        if isPossible:
            answer += 1
    return answer
