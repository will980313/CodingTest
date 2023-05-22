def solution(s):
    answer = []
    alp_dict = {}
    for i, c in enumerate(s):
        if c in alp_dict:
            answer.append(i - alp_dict[c])
            alp_dict[c] = i
        else:
            answer.append(-1)
            alp_dict[c] = i
    return answer