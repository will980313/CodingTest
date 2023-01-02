n,m = map(int, input().split())
answer = 0
rect_mat = []
for _ in range(n):
    rect_mat.append(input())
for i, row in enumerate(rect_mat):

    for j_1, s_1 in enumerate(row):
        for j_2, s_2 in enumerate(row):
            if s_1 == s_2 and j_1 < j_2:
                length =  j_2 - j_1
                if length+i < n and rect_mat[i+length][j_1] == s_1 and rect_mat[i+length][j_2] == s_2 and answer < length:
                    answer = length
print((answer+1)**2)