def solution(s):
    answer = 1
    c_x = 1
    c_not_x = 0
    x = s[0]
    for i in s[1:]:
        if c_x == c_not_x:
            answer+=1
            x = i
            c_x = 0
            c_not_x = 0
        if i == x:
            c_x+=1
        else:
            c_not_x+=1
        
            
    return answer