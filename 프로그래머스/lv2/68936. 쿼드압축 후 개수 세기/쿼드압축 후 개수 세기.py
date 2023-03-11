def compression(arr, answer):
    for row in arr:
        for num in row:
            if num != arr[0][0]:
                break
        else:
            continue
        break
    else:
        answer[arr[0][0]]+=1
        return
    res = [[[] for _ in range(len(arr)//2)] for _ in range(4)]
    for i, row in enumerate(arr):
        for j, num in enumerate(row):
            res[i//(len(arr)//2) * 2 + j//(len(arr)//2)][i%(len(arr)//2)].append(num)
    for cell in res:
        compression(cell, answer)
        
def solution(arr):
    answer = {1:0,0:0}
    compression(arr, answer)
    return list(answer.values())[::-1]