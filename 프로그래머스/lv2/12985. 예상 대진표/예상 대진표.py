def solution(n,a,b):
    answer = 0
    a-=1
    b-=1
    for i in range(n//2):
        if a//2 == b//2:
            answer = i+1
            break
        a = a//2
        b = b//2

    return answer