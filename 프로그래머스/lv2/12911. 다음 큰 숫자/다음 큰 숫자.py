def solution(n):
    answer = n
    num = len(bin(n)) - len(bin(n).replace('1',''))
    while True:
        answer+=1
        if num == len(bin(answer)) - len(bin(answer).replace('1','')):
            break
    return answer