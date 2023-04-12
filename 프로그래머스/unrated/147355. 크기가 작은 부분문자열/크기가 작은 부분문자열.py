def solution(t, p):
    return sum([1 for i in range(len(p),len(t)+1) if int(t[i-len(p):i]) <= int(p) ])