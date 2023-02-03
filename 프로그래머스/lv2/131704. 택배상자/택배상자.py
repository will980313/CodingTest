def solution(order):
    answer = 0
    main = [i for i in range(len(order),0,-1)]
    sub = []
    for i in order:
        while True:
            if main and main[-1] == i:
                answer+=1
                main.pop()
                break
            if sub and sub[-1] == i:
                answer+=1
                sub.pop()
                break
            if main:
                sub.append(main.pop())
            else:
                return answer
    return answer