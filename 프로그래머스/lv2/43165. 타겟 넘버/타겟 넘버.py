
def solution(numbers, target):
    answer = {'1':0}
    def dfs(i, cal, g):
        if i == len(g):
            if cal == target:
                answer['1']+=1
            return 
        v = g[i]
        dfs(i+1, cal + v, g)
        dfs(i+1, cal - v, g)
    dfs(0,0,numbers)
    return answer['1']