import collections

def solution(participant, completion):
    collect = collections.Counter(participant) - collections.Counter(completion)
    return list(collect.keys())[0]

def solution2(participant, completion):

    participant.sort()
    completion.sort()
    
    for p, c in zip(participant, completion):
        if p != c:
            return p

    return participant[-1]

def solution3(participant, completion):

    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if completion[i] != participant[i]:
            return participant[i]

    return participant[-1]
