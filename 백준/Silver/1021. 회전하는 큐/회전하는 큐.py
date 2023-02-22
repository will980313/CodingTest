from collections import deque
n, m = map(int,input().split())
target = list(map(int,input().split()))
que = deque([i+1 for i in range(n)])
answer = 0
for i in target:
    while  que[0] != i:
        if que.index(i) < len(que)//2 + 1:
            que.append(que.popleft())
            answer+=1
        else:
            que.appendleft(que.pop())
            answer+=1
    que.popleft()
print(answer)