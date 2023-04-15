def solution(n):
    temp = ''
    answer = 0
    while n:
        temp+=str(n%3)
        n//=3
    for i, num in enumerate(str(int(temp))[::-1]):
        answer+= int(num) * 3**i
    return answer