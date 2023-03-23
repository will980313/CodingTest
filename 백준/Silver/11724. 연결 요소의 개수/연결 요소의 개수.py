from collections import deque
import sys
def bfs(graph, n):
    visited = [False for _ in range(n)]
    answer = 0
    for i in range(n):
        if visited[i]:
            continue
        que = deque([i])
        visited[i] = True
        while que:
            now = que.popleft()
            for num in graph[now]:
                if visited[num] == False:
                    visited[num] = True
                    que.append(num)
        answer+=1
    return answer

n, m = map(int,input().split())
graph = {i:[] for i in range(n)}
for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
print(bfs(graph,n))