def solution(arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        temp = []
        for ik, jk in zip(i,j):
            temp.append(ik+jk)
        answer.append(temp)
            
    return answer