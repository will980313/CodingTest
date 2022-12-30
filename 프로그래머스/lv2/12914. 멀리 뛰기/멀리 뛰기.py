def solution(n):
    answer = 0
    arr = [0]*(n+1)
    arr[0] = 1
    arr[1] = 2
    if(n >2):
        for i in range (3, n+1):
            arr[i-1] = arr[i-2]+ arr[i -3]
    answer = arr[n-1]

    return answer%1234567