from collections import Counter
def solution(N, stages):
    temp = len(stages)
    stages_dict = Counter(stages)
    answer = []
    for i in range(1,N+1):
        if i not in stages_dict:
            stages_dict[i] = 0
        if temp == 0:
            answer.append((i, 0))
            continue
        answer.append((i, stages_dict[i]/temp))
        temp -= stages_dict[i]
    answer = [i[0] for i in sorted(answer, reverse = True, key = lambda x: x[1])]
    return answer