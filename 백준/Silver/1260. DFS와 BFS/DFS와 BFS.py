from collections import deque
def dfs(graph, start):
    visited = [False]* (len(graph) + 1)
    que = deque([start])
    answer = []
    while len(que) > 0:
        temp = que.pop()
        if visited[temp]:
            continue
        visited[temp] = True
        answer.append(temp)
        graph[temp].sort(reverse = True)
        for i in graph[temp]:
            que.append(i)
    return ' '.join(list(map(str,answer)))

def bfs(graph, start):
    visited = [False]* (len(graph) + 1)
    que = deque([start])
    answer = []
    while len(que) > 0:
        temp = que.popleft()
        if visited[temp]:
            continue
        visited[temp] = True
        answer.append(temp)
        graph[temp].sort()
        for i in graph[temp]:
            que.append(i)
    return ' '.join(list(map(str,answer)))


n, r ,start = map(int,input().split())
graph = {i+1:[] for i in range(n)}
for _ in range(r):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
print(dfs(graph, start))
print(bfs(graph, start))
