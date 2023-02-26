def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0
    for i in range(len(score)//m):
        answer+=min(score[i*m:(i+1)*m])*m
    return answer