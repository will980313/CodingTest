def solution(board):
    m = len(board)
    n = len(board[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[0] = board[0]
    for i, row in enumerate(board):
        dp[i][0] = row[0] 
    for i in range(1,m):
        for j in range(1,n):
            if board[i][j]:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
    answer = 0
    for i in range(len(dp)):
        temp = max(dp[i])
        if temp > answer:
            answer = temp
    return answer * answer