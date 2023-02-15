def n_queens (i, col):
    n = len(col) - 1
    if (promising(i, col)):
        if (i == n):
            col[0]+=1
        else:
            for j in range(1, n+1):
                col[i + 1] = j
                n_queens(i+1, col)

def promising (i, col):
    k = 1
    while(k<i):
        if(col[i] == col[k] or abs(col[i] - col[k]) == (i-k)):
            return False
        k += 1
    return True

def solution(n):
    col = [0] * (n+1)
    n_queens(0,col)
    return col[0]