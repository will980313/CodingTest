from collections import deque
def bfs(n, graph):
    answer = [0, 9999]
    for i in range(1, n+1):
        que = deque([[i,1]])
        temp = [0 for _ in range(n)]
        temp[i-1] = 1
        while que:
            now, count = que.popleft()
            for num in graph[now]:
                if temp[num-1] > count or temp[num-1] == 0:
                    temp[num-1] = count
                if 0 in temp:
                    que.append([num, count + 1])
        if sum(temp) - 1 < answer[1]:
            answer = [i,sum(temp) - 1]
    return answer[0]
n, m = map(int, input().split())
graph = {i:[] for i in range(1,n+1)}
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
print(bfs(n, graph))