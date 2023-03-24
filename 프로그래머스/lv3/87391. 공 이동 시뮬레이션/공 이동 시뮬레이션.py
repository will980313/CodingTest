def solution(n, m, x, y, queries):
    answer = 0
    x_1 = x
    x_2 = x
    y_1 = y
    y_2 = y
    for query in queries[::-1]:
        if query[0] == 0:
            if y_2 + query[1] < m:
                y_2 += query[1]
            else:
                y_2 = m-1
            if y_1 != 0:
                y_1 += query[1]
        elif query[0] == 1:
            if y_1 - query[1] >= 0:
                y_1 -= query[1]
            else:
                y_1 = 0
            if y_2 != m-1:
                y_2 -= query[1]
        elif query[0] == 2:
            if x_2 + query[1] < n:
                x_2 += query[1]
            else:
                x_2 = n-1
            if x_1 != 0:
                x_1 += query[1]
        elif query[0] == 3:
            if x_1 - query[1] >= 0:
                x_1 -= query[1]
            else:
                x_1 = 0
            if x_2 != n-1:
                x_2 -= query[1]
        if x_2 < 0 or x_1 >= n or y_2 <0 or y_1 >=m:
            return 0
    return (x_2 - x_1 + 1) * (y_2 - y_1 + 1)