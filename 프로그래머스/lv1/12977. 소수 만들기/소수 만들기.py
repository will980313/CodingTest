from itertools import combinations

def check(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return 0
    return 1

def solution(nums):
    nums = combinations(nums,3)
    return sum([check(sum(i)) for i in nums])