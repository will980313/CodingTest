from collections import Counter
def solution(topping):
    answer = 0
    dict_chul = Counter(topping)
    set_bro = set()
    while len(topping) > 0:
        temp = topping.pop()
        set_bro.add(temp)
        dict_chul[temp] -= 1
        if dict_chul[temp] == 0:
            del dict_chul[temp]
        if len(set_bro) == len(dict_chul):
            answer+=1
    return answer