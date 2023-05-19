def mul(n):
    res = 1
    for i in n:
        res*=i
    return res

def solution(num_list):
    return 1 if mul(num_list) < sum(num_list)**2 else 0