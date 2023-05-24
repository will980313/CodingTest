def solution(k, score):
    answer = []
    for i in range(1,len(score)+1):
        temp = sorted(score[:i], reverse = True)
        answer.append(temp[:k].pop())
    return answer