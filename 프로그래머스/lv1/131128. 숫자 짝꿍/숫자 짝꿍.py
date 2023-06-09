def solution(X, Y):
    answer = ''
    for i in range(9, -1, -1):
        temp = min(X.count(str(i)), Y.count(str(i)))
        answer = ''.join([answer,str(i)*temp])
    zero = answer.count('0')
    if zero > 0 and zero == len(answer):
        return '0'
    return answer if len(answer) else '-1'