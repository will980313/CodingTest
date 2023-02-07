from collections import deque
def bfs(graph, K):
    visited = [0] * len(graph)
    que = deque([1])
    answer = 0
    while que:
        loc = que.popleft()
        for i, d in graph[loc]:
            if i == 1:
                continue
            if visited[i -1] == 0:
                visited[i -1] = visited[loc-1] + d
                que.append(i)
            elif visited[i -1] > visited[loc-1] + d:
                visited[i -1] = visited[loc-1] + d
                que.append(i)
    for i in visited:
        if i <= K:
            answer+=1
    return answer 

def solution(N, road, K):
    graph = {i+1:[] for i in range(N)}
    for a, b, dis in road:
        if b not in graph[a]:
            graph[a].append((b,dis))
        if a not in graph[b]:
            graph[b].append((a,dis))
    return bfs(graph,K)