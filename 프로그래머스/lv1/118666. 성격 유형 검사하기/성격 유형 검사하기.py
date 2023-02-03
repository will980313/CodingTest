def solution(survey, choices):
    answer = ''
    list_cat = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    dic_cat = {i:0 for i in list_cat}
    for n,s in zip(survey,choices):
        if s > 4:
            dic_cat[n[0]]+= s - 4
        elif s < 4:
            dic_cat[n[1]]+= 4 - s
    for i, j in zip(list_cat[::2],list_cat[1::2]):
        if dic_cat[i] < dic_cat[j]:
            answer+=(i)
        elif dic_cat[i] > dic_cat[j]:
            answer+=(j)
        else:
            answer+=(i)
    return answer