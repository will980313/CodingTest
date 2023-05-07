from collections import deque

def solution(queue1, queue2):
    tar = sum(queue1 + queue2)//2
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    c = 0
    val = sum(queue1)
    while queue2:
        if val < tar:
            queue1.append(queue2.popleft())
            val+= queue1[-1]
            c+=1
        elif val == tar:
            return c
        else:
            val-= queue1.popleft()
            c+=1
    return -1