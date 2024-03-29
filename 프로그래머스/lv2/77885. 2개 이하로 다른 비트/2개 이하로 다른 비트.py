def solution(numbers):
    answer = []
    for i in numbers:
        if i%2 ==0:
            answer.append(i+1)
            continue
        if bin(i).count('0') == 0:
            answer.append(2**(bin(i).count('1')-1) + i)
            continue
        count = 0
        for j in bin(i)[::-1]:
            if j != '1':
                break
            count+=1
        answer.append(2**(count-1) + i)
    return answer