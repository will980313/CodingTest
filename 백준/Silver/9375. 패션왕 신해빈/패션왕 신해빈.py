n = int(input())

for _ in range(n):
    wears = {}
    answer = 1
    m = int(input())
    for _ in range(m):
        temp = input().split()[1]
        if temp not in wears:
            wears[temp] = 1
        else:
            wears[temp]+=1
    for w in wears:
        answer*=wears[w]+1
    answer-=1
    print(answer)