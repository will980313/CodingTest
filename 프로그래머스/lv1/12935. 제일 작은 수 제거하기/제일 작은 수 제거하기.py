def solution(arr):
    min_num = min(arr)
    del arr[arr.index(min_num)]
    return [-1] if len(arr) == 0 else arr