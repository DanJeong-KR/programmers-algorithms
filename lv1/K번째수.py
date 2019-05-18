# 쉬운 방법
def solution(array, commands):
    answer = []
    for cmd in commands:
        answer.append(sorted(array[cmd[0]-1:cmd[1]])[cmd[2]-1])
    return answer

# 람다식
def solution2(array, commands):
    return list(map(lambda cmd: sorted(array[cmd[0]-1:cmd[1]])[cmd[2]-1], commands))
    # or
    return list(
                map(
                    lambda cmd: sorted(array[cmd[0]-1:cmd[1]])[cmd[2]-1],
                    commands
                )
            )
