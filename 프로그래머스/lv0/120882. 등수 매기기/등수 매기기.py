def solution(score):
    score = [(i+j)/2 for i, j in score]
    sort_score = sorted(score,reverse = True)
    return [sort_score.index(i)+1 for i in score]