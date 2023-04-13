import itertools
def solution(number):
    return sum([1 for i in itertools.combinations(number, 3) if sum(i) == 0])