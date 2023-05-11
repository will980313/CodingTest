def solution(plans):
    answer = []
    stack = []
    for i in range(len(plans)):
        temp = plans[i][1].split(':')
        plans[i][1] = int(temp[0]) * 60 + int(temp[1])
        plans[i][2] = int(plans[i][2])
    plans.sort(key = lambda x: x[1])
    while plans:
        now = plans.pop(0)
        if plans and now[1] + now[2] > plans[0][1]:
            now[2] -=  plans[0][1] - now[1]
            stack.append(now)
        elif plans and now[1] + now[2] == plans[0][1]:
            answer.append(now[0])
        elif plans and now[1] + now[2] < plans[0][1]:
            answer.append(now[0])
            temp = plans[0][1] - now[1] - now[2]
            while temp > 0 and stack:
                if stack[-1][2] <= temp:
                    temp -= stack[-1][2]
                    answer.append(stack[-1][0])
                    stack.pop()
                else:
                    stack[-1][2]-=temp
                    break
        else:
            answer.append(now[0])
    return answer + [i[0] for i in stack[::-1]]