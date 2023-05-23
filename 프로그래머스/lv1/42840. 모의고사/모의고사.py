def solution(answers):
    answer = {1:0, 2:0, 3:0}
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 1, 2, 3, 2, 4, 2, 5]
    arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i, n in enumerate(answers):
        if n == arr1[i%5]:
            answer[1]+=1
        if n == arr2[i%8]:
            answer[2]+=1
        if n == arr3[i%10]:
            answer[3]+=1
    return [i for i in answer if answer[i] == max(answer.values())]