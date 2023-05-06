def cal(n):
    res = 0
    for i in range(1,n+1):
        if n%i ==0:
            res+=1
    if res%2 == 0:
        return n
    return -n

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        answer+= cal(i)
    return answer