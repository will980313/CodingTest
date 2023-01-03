input()
str_S = input().split()
S = []
for num in str_S:
    num = int(num)
    S.append(num)
n = int(input())
A = 0
B = 0
S.sort()
for num in S:
    if num > n:
        B = num
        break
    A = num
answer = 0
for i in range(A+1, B):
    for j in range(i+1,B):
        if i<= n and n <= j:
            answer += 1
print(answer)