def solution(n, m):
    answer = []
    for i in range(min(m,n), 0, -1):
        if n%i == 0 and m%i == 0:
            answer.append(i)
            break
    for i in range(max(m,n), m*n+1):
        if i%n == 0 and i%m == 0:
            answer.append(i)
            break
    return answer