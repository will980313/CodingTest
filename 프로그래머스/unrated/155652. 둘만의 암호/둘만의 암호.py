import string 
def solution(s, skip, index):
    list_alp = [i for i in string.ascii_lowercase if not i in skip]
    dict_alp1 = {i:n for i, n in enumerate(list_alp+list_alp+list_alp)}
    dict_alp2 = {n:i for i, n in enumerate(list_alp)}
    answer = ''
    for i in s:
        if i in skip:
            continue
        answer+=dict_alp1[dict_alp2[i]+index]
    return answer