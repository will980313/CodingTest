from collections import deque
def bfs(n,m):
    que = deque([(n,0)])
    visited = [False for _ in range(100001)]
    while que:
        now, dis = que.popleft()
        visited[now] = True
        if now == m:
            return dis
        if now-1>=0 and visited[now-1] == False:
            que.append((now-1,dis+1))
        if now+1>=0 and now+1 < 100001 and visited[now+1] == False:
            que.append((now+1,dis+1))
        if now*2>=0 and now*2 < 100001 and visited[now*2] == False:
            que.append((now*2,dis+1))
n,m = map(int,input().split())
print(bfs(n,m))