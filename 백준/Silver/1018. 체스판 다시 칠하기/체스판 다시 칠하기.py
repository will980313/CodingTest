m, n = map(int, input().split())
board = []
answer = 9999
switch = ['W', 'B']
for _ in range(m):
    board.append(input())
for c in switch:
    for i in range(m - 8+1):
        for j in range(n - 8+1):
            temp = 0
            for x in range(i,8+i):
                for y in range(j,8+j):
                    if ((x-i) +(y-j))%2==0 and board[x][y] != c:
                        temp+=1
                    elif ((x-i) +(y-j))%2==1 and board[x][y] == c:
                        temp+=1
            if temp < answer:
                answer = temp
print(answer)