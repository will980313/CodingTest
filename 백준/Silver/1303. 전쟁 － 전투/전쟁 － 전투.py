n, m = map(int,input().split())
board = [input() for _ in range(m)]
visited = [[True for _ in range(n)] for _ in range(m)]
answer = {'W':0, 'B':0}
for i in range(m):
    for j in range(n):
        if visited[i][j] == False:
            continue
        temp = 1
        visited[i][j] = False
        que = [(i,j)]
        while que:
            y,x = que.pop()
            if y != m-1 and visited[y+1][x] and board[y][x] == board[y+1][x]:
                temp+=1
                visited[y+1][x] = False
                que.append((y+1,x))
            if x != n-1 and visited[y][x+1] and board[y][x] == board[y][x+1]:
                temp+=1
                visited[y][x+1] = False
                que.append((y,x+1))
            if y != 0 and visited[y-1][x] and board[y][x] == board[y-1][x]:
                temp+=1
                visited[y-1][x] = False
                que.append((y-1,x))
            if x != 0 and visited[y][x-1] and board[y][x] == board[y][x-1]:
                temp+=1
                visited[y][x-1] = False
                que.append((y,x-1))
        answer[board[i][j]] += temp**2
print(answer['W'], answer['B'])