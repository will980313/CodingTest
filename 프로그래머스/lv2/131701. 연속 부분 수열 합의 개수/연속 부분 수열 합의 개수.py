def solution(elements):
    answer = []
    elements+=elements
    for i in range(len(elements)//2):
        for j in range(len(elements)//2):
            answer.append(sum(elements[j:j+i]))
    return len(set(answer))