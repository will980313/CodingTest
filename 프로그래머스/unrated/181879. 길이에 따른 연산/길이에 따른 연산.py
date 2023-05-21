def mul(num_list):
    res = 1
    for i in num_list:
        res*=i
    return res

def solution(num_list):
    return sum(num_list) if len(num_list) > 10 else mul(num_list)