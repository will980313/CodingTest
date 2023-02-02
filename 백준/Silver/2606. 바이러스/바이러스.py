from collections import deque
def dfs(graph, start):
    que = deque([start])
    visited = [False] * (len(graph)+1)
    answer = -1
    while que:
        temp = que.popleft()
        if visited[temp]:
            continue
        visited[temp] = True
        for i in graph[temp]:
            que.append(i)
        answer+=1
    return answer


c = int(input())
n = int(input())
graph = {i+1:[] for i in range(c)}

for _ in range(n):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
print(dfs(graph, 1))