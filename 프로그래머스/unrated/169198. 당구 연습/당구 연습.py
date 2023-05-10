def solution(m, n, startX, startY, balls):
    answer = []
    for i,j in balls:
        move = [(-i,j),(i,-j),(i+(m-i)*2,j),(i,j+(n-j)*2)]
        dis=[]
        for x,y in move:
            res_dis = (x - startX)**2 + (y - startY)**2
            ball_dis = (i - x)**2 + (j - y)**2
            if x==startX and ball_dis < res_dis or y==startY and ball_dis < res_dis:
                continue
            dis.append(res_dis)
        answer.append(min(dis))
    return answer