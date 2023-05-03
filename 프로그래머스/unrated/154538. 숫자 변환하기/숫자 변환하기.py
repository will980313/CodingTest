from collections import deque

def trance(x,y,n,c):
    que = deque([(y, c)])
    answer = []
    while que:
        y, c = que.popleft()
        if x == y:
            return c
        c+=1
        sub_n = y-n
        div_2 = y//2
        div_3 = y//3
        if sub_n >= x:
            que.append((sub_n, c)) 
        if div_2 >= x and y%2 == 0:
            que.append((div_2, c)) 
        if div_3 >= x and y%3 == 0:
            que.append((div_3, c)) 
    return -1

def solution(x, y, n):
    return trance(x,y,n,0)