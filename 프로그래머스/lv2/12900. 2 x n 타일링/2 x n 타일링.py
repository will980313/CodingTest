def solution(n):
    answer = [1,2]
    for i in range(2,n):
        answer[0] = answer[0] + answer[1]
        answer[1] , answer[0] = answer[0] , answer[1]
    return answer[-1]%1000000007