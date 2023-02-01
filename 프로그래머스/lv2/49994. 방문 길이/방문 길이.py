def solution(dirs):
    answer = []
    loc = [0,0]
    for i in dirs:
        temp = loc[:]
        if i == 'U':
            loc[1]+=1
        elif i =='D':
            loc[1]-=1
        elif i == 'L':
            loc[0]-=1
        elif i == 'R':
            loc[0]+=1
        if abs(loc[0]) == 6 or abs(loc[1]) == 6:
            loc = temp[:]
            continue
        if (str(temp)+str(loc)) not in answer:
            answer.append(str(temp)+str(loc))
            answer.append(str(loc)+str(temp))
    return len(answer)//2