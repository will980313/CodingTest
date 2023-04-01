def solution(numbers):
    return sum(set([i for i in range(10)]) - set(numbers))