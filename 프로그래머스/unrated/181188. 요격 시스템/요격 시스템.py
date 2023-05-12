def solution(targets):
    answer = 1
    targets.sort(key = lambda x: x[1])
    dis = targets[0]
    for s, e in targets[1:]:
        if dis[0] < s <dis[1] or dis[0] < e <dis[1] or s< dis[0] <e or s< dis[1] <e:
            dis = [max(dis[0], s), min(dis[1], e)]
        else:
            dis = [s,e]
            answer+=1
    return answer