def solution(d, budget):
    d.sort()
    answer = 0
    for i in d:
        if i <= budget:
            answer+=1
            budget-=i
    return answer