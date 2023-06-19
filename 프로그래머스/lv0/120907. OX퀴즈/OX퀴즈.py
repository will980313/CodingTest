def solution(quiz):
    answer = []
    for i in quiz:
        i = i.split()
        temp = int(i[0])
        if i[1] == '-':
            temp-= int(i[2])
        else:
            temp+= int(i[2])
        if temp == int(i[-1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer