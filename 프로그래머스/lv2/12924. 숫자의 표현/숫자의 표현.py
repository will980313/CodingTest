def solution(n):
    answer = 0
    for i in range(1,n):
        for j in range(i, n+1):
            num = (i+j)*(j-i+1)/2
            if num ==n:
                answer+=1
                break
            elif num > n:
                break
    return answer+1