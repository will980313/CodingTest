def solution(s):
    answer = []
    s_list = s[2:-2].split('},{')
    s_list = sorted(s_list,key = lambda x: len(x))
    answer.append(int(s_list[0].split(',')[0]))
    for i in range(len(s_list) - 1):
        answer.append(list(set(list(map(int,s_list[i+1].split(',')))).difference(set(list(map(int,s_list[i].split(','))))))[0])
    return answer