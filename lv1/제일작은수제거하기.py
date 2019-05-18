def solution(arr):
    if len(arr) == 1:
        return [-1]
    del arr[arr.index(min(arr))]
    return arr

def solution2(arr):
    if len(arr) == 1:
        return [-1]
    arr.remove(min(arr))
    return arr
