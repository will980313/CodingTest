def solution(n):
    p = [0,1]
    for i in range(n-1):
        p.append(sum(p[-2:]))
    return p[-1]%1234567