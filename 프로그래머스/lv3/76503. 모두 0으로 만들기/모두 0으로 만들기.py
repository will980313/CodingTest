def search(graph_len, a, graph, que):
    answer = 0
    if sum(a) !=0:
        return -1
    while len(que):
        i = que.pop()
        for j in graph[i]:
            if j in graph_len.keys():
                graph_len[j]-=1
                a[j] += a[i]
                if graph_len[j] == 1:
                    que.append(j)
                del graph_len[i]
                break
        answer+=abs(a[i])
        a[i] = 0
    return answer

def solution(a, edges):
    graph = {i: [] for i in range(len(a))}
    answer = []
    for e in edges:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    graph_len = {}
    que = []
    for i in range(len(a)):
        graph_len[i] = len(graph[i])
        if graph_len[i] ==1:
            que.append(i)
    answer = search(graph_len, a, graph, que)
    return answer