def solution(brown, yellow):
    answer = []
    num = (brown+4)//2
    for i in range(3,num):
        x = i
        y = num - i
        if (x-2) * (y-2) == yellow:
            answer = [x,y]
            break
    answer.sort(reverse=True)
    return answer