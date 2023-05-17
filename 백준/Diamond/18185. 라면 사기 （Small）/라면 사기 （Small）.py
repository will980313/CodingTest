n = int(input())
fact = list(map(int,input().split()))
answer = 0
for i in range(n-2):
    if fact[i+1] > fact[i+2]:
        temp = min(fact[i],fact[i+1]-fact[i+2])
        answer+=temp*5
        fact[i] -= temp
        fact[i+1] -= temp
    if fact[i] > 0 and fact[i+1] > 0 and fact[i+2] > 0:
        temp = min(fact[i],fact[i+1],fact[i+2])
        answer += temp*7
        fact[i]-=temp
        fact[i+1]-=temp
        fact[i+2]-=temp
    if fact[i]>0:
        answer += fact[i]*3

if fact[-1]>0 and fact[-2]>0:
    temp = min(fact[-2:])
    answer+=temp*5
    fact[-2]-=temp
    fact[-1]-=temp
    answer+=max(fact[-2:])*3

elif fact[-1]>0 or fact[-2]>0:
    answer+=max(fact[-2:])*3
print(answer)