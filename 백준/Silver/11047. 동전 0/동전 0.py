n, money = map(int,input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
answer = 0
for i in coin[::-1]:
    temp = money//i
    if temp:
        money%=i
        answer+=temp
    if money == 0:
        break
print(answer)