from collections import deque

def solution(s):
    answer = 0
    s = deque(s)
    for _ in range(len(s)):
        temp = ['a']
        for i in s:
            if i ==")" and temp[-1] == "(":
                del temp[-1]
            elif i =="}" and temp[-1] == "{":
                del temp[-1]
            elif i =="]" and temp[-1] == "[":
                del temp[-1]
            else:
                temp.append(i)

        if len(temp) == 1:
            answer+=1
        
        s.appendleft(s.pop())
    return answer