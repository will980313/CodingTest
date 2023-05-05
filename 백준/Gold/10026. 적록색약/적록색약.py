def dfs(graph):
    visited = [[False for _ in range(len(graph))] for _ in range(len(graph))]
    answer=0
    for i in range(len(graph)):
        for j in range(len(graph)):
            if visited[i][j]:
                continue
            que = [(i,j)]
            while que:
                idx = que.pop()
                now = graph[idx[0]][idx[1]]
                if idx[0] != 0 and not visited[idx[0]-1][idx[1]] and graph[idx[0]-1][idx[1]]==now:
                    visited[idx[0]-1][idx[1]] = True
                    que.append((idx[0]-1,idx[1]))
                if idx[0] != len(graph)-1 and not visited[idx[0]+1][idx[1]] and graph[idx[0]+1][idx[1]]==now:
                    visited[idx[0]+1][idx[1]] = True
                    que.append((idx[0]+1,idx[1]))  
                if idx[1] != 0 and not visited[idx[0]][idx[1]-1] and graph[idx[0]][idx[1]-1]==now:
                    visited[idx[0]][idx[1]-1] = True
                    que.append((idx[0],idx[1]-1)) 
                if idx[1] != len(graph)-1 and not visited[idx[0]][idx[1]+1] and graph[idx[0]][idx[1]+1]==now:
                    visited[idx[0]][idx[1]+1] = True
                    que.append((idx[0],idx[1]+1)) 
            answer+=1
    return answer
n = int(input())
graph = []
graph2 = []
for _ in range(n):
    row = input()
    graph.append(row)
    graph2.append(row.replace('G','R'))
print(dfs(graph),dfs(graph2))