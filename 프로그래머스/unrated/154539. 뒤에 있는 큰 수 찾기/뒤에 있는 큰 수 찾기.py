def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    stack = []
    for i, n in enumerate(numbers):
        while stack and numbers[stack[-1]] < n:
            answer[stack.pop()] = n
        stack.append(i)
    return answer