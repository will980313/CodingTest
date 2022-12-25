def solution(s):
    answer = 0
    stack = ['']
    for c in s:
        if stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    if len(stack) == 1:
        answer = 1
    return answer