def solution(land):
    answer = land[0]
    for i, arr in enumerate(land[1:]):
        temp = [0,0,0,0]
        temp[0] = max(answer[1],answer[2],answer[3]) + arr[0]
        temp[1] = max(answer[0],answer[2],answer[3]) + arr[1]
        temp[2] = max(answer[0],answer[1],answer[3]) + arr[2]
        temp[3] = max(answer[0],answer[1],answer[2]) + arr[3]
        answer = temp
    return max(answer)