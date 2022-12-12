import math
def solution(progresses, speeds):
    progresses = [math.ceil((100 - i) / j) for i,j in zip(progresses,speeds)] 
    answer = []
    temp = progresses[0]
    progresses.append(999)
    count = 1
    for i in progresses[1:]:
        if temp >= i:
            count+=1
            continue
        else:
            answer.append(count)
            count = 1
        temp = i
    return answer