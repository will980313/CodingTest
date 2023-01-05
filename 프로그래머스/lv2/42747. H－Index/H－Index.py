def solution(citations):
    citations.sort()
    answer = 0
    for i in range(citations[-1]):
        up =0
        for j in citations:
            if i <= j:
                up+=1
        if up >= i:
            answer = i
    return answer