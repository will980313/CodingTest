def solution(id_list, report, k):
    answer = []
    dict_name = {i:[] for i in id_list}
    dict_report = {i:0 for i in id_list}
    for i in report:
        a,b = i.split()
        if b not in dict_name[a]:
            dict_name[a].append(b)
    for i in dict_name:
        for j in dict_name[i]:
            dict_report[j]+=1
    for i in dict_name:
        temp = 0
        for j in dict_name[i]:
            if dict_report[j] >= k:
                temp+=1
        answer.append(temp)
    return answer