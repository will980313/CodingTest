def solution(arr1, arr2):
    answer = []
    arr2 = [list(i) for i in zip(*arr2)]
    for i in arr1:
        temp1=[]
        for j in arr2:
            temp2=0
            for k in range(len(arr1[0])):
                temp2 +=i[k]*j[k]
            temp1.append(temp2)
        answer.append(temp1)
    return answer