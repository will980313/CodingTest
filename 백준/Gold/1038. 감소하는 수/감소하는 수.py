def check(answer):
    for i in range(9, -1,-1):
        if answer[i-1] - answer[i] > 1 or answer[i]!=9 and answer[i-1]==0 and answer[i]!=0 or answer[i]!=9 and answer[i-1]==0 and i==9:
            answer[i]+=1
            for j in range(1, 10 - i):
                answer[-j] = j-1
            break
        elif answer[i]==0 and answer[i-1]==0 or answer[i]==0 and i==0:
            for j in range(1, 11 - i):
                answer[-j] = j-1
            break
n = int(input())
count = 0
answer = [0 for _ in range(10)]
for _ in range(n):
    if answer == [9,8,7,6,5,4,3,2,1,0]:
        answer = [-1]
        break
    check(answer)
answer = int(''.join(list(map(str,answer))))
print(answer)