def transe(q,n):
    NOTATION = '0123456789ABCDEF'
    s = ''
    while q > 0:
        q, mod = divmod(q,n)
        s += NOTATION[mod]
    return s[::-1]

def solution(n, t, m, p):
    answer = '0'
    for i in range(1, t*m):
        answer+=transe(i,n)
    return answer[p-1:t*m+p-1:m]