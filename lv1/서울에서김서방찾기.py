def solution(seoul):
    for x, name in enumerate(seoul):
        if name == 'Kim':
            return '김서방은 ' + str(x) + '에 있다'

def solution2(seoul):
    return '김서방은 {}에 있다'.format(seoul.index('Kim'))
