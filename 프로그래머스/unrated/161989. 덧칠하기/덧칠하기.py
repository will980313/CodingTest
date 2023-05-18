def solution(n, m, section):
    answer = 0
    temp = 0
    while section:
        if temp==0 or section[0] >= temp+m:
            temp = section.pop(0)
            answer+=1
        else:
            section.pop(0)

    return answer