def solution(arr, idx):
    return arr[idx:].index(1)+idx if 1 in arr[idx:] else -1