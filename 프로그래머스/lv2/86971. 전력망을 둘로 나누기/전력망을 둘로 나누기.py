from collections import deque
def bfs (graph, node, visited, remove):
    queue = deque([node])
    visited[node] = True
    count = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if remove == [v, i] or remove == [i,v]:
                continue
            if not (visited[i]):
                queue.append(i)
                visited[i] = True
                count+=1
    return count
def solution(n, wires):
    answer = 100
    graph = []
    
    for i in range(n+1):
        temp = []
        for node in wires:
            if i in node:
                if node[0] == i:
                    temp.append(node[1])
                else:
                    temp.append(node[0])
        graph.append(temp)      
    for i in wires:
        visited = [False] * (n+1)
        count = bfs(graph, 1, visited, i)
        if abs(n - 2*count) < answer:
            answer = abs(n - 2*count)


    return answer