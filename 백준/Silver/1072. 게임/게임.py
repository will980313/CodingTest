x,y = map(int, input().split())
temp = int(y* 100/x )
l = 0
r = 10000000000
count =0
while r - l != 0 :
    count = (r - l)//2 + l
    if int((y+count)* 100/(x+count) ) > temp:
        r = count
        if r-1==l:
            break
    else:
        l = count
        if r-1==l:
            break
if r == 10000000000:
    r = -1
print(r)



