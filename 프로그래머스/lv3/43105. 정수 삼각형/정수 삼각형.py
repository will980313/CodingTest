def solution(triangle):
    answer = 0
    for i in range(1,len(triangle)):
        for j in range(i+1):
            if j -1 >= 0:
                triangle[i][j]+=max(triangle[i-1][j-1:j+1])
            else:
                triangle[i][j]+=triangle[i-1][j]
    return max(triangle[-1])