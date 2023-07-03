def solution(my_string):
    my_string = my_string.split()
    answer = int(my_string[0])
    for i in range(1, len(my_string)):
        if my_string[i] == '+':
            answer += int(my_string[i+1])
        elif my_string[i] == '-':
            answer -= int(my_string[i+1])
        else:
            continue
    return answer