def solution(number, k):
    answer = []
    for c in number:
        while answer and answer[-1] < c and k > 0:
            answer.pop()
            k-=1
        answer.append(c)
    if k != 0:
        answer = answer[:-k]
    return ''.join(answer)