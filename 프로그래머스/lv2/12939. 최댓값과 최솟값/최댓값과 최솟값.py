def solution(s):
    num =[int(i) for i in s.split()]
    
    answer = f'{min(num)} {max(num)}'
    return answer