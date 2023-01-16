def solution(n, left, right):
    answer = []

    for i in range(left//n,right//n+1):
        for j in range(1,n+1):
            if j < i+1:
                answer.append(i+1)
            else:
                answer.append(j)
    return answer[left%n : left%n + (right- left) + 1]