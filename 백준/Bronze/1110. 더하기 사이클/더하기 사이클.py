n = input()
count = 0
ans = n[:]
while True:
    if len(n)==1:
        n ='0'+n
    a = int(n[0])
    b = int(n[1])
    n = str(b) + str(a+b)[-1]
    count+=1
    if int(n) == int(ans):
        break
print(count)