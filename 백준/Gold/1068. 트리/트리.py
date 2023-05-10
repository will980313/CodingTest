def dfs(graph, root):
    que = [root]
    count = 0
    while que:
        now = que.pop()
        if len(graph[now]) == 0:
            count+=1
        for i in graph[now]:
            que.append(i)
    return count

n = int(input())
nodes = list(map(int, input().split()))
root = nodes.index(-1)
del_node = int(input())
if del_node == root:
    print(0)
else:
    nodes[del_node] = -1
    graph = {i:[] for i in range(n)}
    for i, node in enumerate(nodes):
        if node != -1:
            graph[node].append(i)
    print(dfs(graph, root))