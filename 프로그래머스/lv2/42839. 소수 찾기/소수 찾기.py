from itertools import permutations
def isprime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2,int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    temp = []
    for i in range(len(numbers)):
        p = permutations(numbers, i+1)
        for j in p:
            j = ''.join(j)
            if int(j) in temp:
                continue
            temp.append(int(j))
            if isprime(int(j)):
                answer+=1
    return answer