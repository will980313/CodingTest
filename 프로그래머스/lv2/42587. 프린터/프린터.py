def solution(priorities, location):
    answer = 0
    val = priorities[location]

    while (1):
        max_val = max(priorities)
        a = priorities.pop(0)
        if (a != val and a == max_val):
            answer += 1
            location -= 1
        elif (a < val):
            location -= 1
        elif (max_val != val):
            priorities.append(a)
            if (location == 0):
                location = len(priorities) - 1
            else:
                location -= 1

        elif (a == val and max_val == val):
            answer += 1
            location -= 1
            if (location == -1):
                break
    
    return answer