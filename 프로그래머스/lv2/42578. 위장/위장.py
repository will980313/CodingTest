def solution(clothes):
    hash = {}
    for _, tp in clothes:
        if hash.get(tp) is None:
            hash[tp] = 2
        else:
            hash[tp] += 1
    answer = 1
    for i in hash:
            answer *= hash[i]
    return answer -1