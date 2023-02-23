l, r =input().split()
answer = 0
for i, j in zip(l,r):
    if i == j  and len(l) == len(r):
        if i == '8':
            answer+=1
    else:
        break
print(answer)