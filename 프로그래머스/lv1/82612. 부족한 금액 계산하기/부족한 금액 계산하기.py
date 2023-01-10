def solution(price, money, count):
    answer = 0
    for i in range(1,count+1):
        answer+=price*i
    if money - answer > 0:
        answer = 0
    else:
        answer = answer - money
    return answer