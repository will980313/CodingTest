def check(num, btns):
    for c in str(num):
        if int(c) in btns:
            return True 
    return False

n = int(input())
k = int(input())
if k:
    btns = list(map(int,input().split()))
else:
    btns = []
temp = n
while check(temp, btns):
    temp+=1
    if temp > 999999:
        temp = 99999999
        break
answer_1 = temp - n + len(str(temp))
temp = n
while check(temp, btns):
    temp-=1
    if temp < 0:
        temp = -99999999
        break
answer_2 = n - temp + len(str(temp))
answer_3 = abs(100 - n)
print(min([answer_1, answer_2, answer_3]))