def solution(babbling):
    words =  ["aya", "ye", "woo", "ma"]
    answer = 0
    for i in babbling:
        for j in words:
            if j in i:
                i = ' '.join(i.split(j))
            if len(i.split()) == 0:
                answer+=1
                break
    return answer