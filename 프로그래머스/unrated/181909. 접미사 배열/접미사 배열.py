def solution(my_string):
    answer = []
    temp = ''
    for i in my_string[::-1]:
        temp = i + temp
        answer.append(temp)
    answer.sort()
    return answer