def solution(s, n):
    answer = ''#65 90 97 122
    for i in s:
        temp = ord(i)
        if temp <= 90 and temp+n > 90:
            answer+= chr(temp+n- 26)
        elif temp <= 122 and temp+n > 122:
            answer+= chr(temp+n- 26)
        elif i ==' ':
            answer+=' '
        else:
            answer+= chr(temp+n)
    return answer