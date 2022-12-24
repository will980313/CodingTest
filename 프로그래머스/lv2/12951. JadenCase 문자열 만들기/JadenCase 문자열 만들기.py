def solution(s):
    answer = ''
    s = s.lower()
    for word in s.split(' '):
        if len(word) != 0:
            answer += word[0].upper()
            answer += word[1:]
        answer += ' '
    
    return answer[:-1]