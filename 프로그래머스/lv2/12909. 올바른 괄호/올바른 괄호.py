def solution(s):
    answer = False
    stack = ""
    for i in s:
        stack += i
        if stack[-2:] =="()":
            stack = stack[:-2]
    if len(stack) ==0:
        answer = True
    return answer
