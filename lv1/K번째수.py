def solution(array, commands):
    answer = []
    for cmd in commands:
        answer.append(sorted(array[cmd[0]-1:cmd[1]])[cmd[2]-1])
    return answer

def solution2(array, commands):
    return list(map(lambda cmd: sorted(array[cmd[0]-1:cmd[1]])[cmd[2]-1], commands))
    # or
    return list(
                map(
                    lambda cmd: sorted(array[cmd[0]-1:cmd[1]])[cmd[2]-1],
                    commands
                )
            )
