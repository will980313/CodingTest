def search(n, l):
    for i in range(l,101):
        temp = n -(i*(i+1)/2)
        if temp % i ==0 and int(temp/i) + 1 >= 0:
            temp = int(temp/i)
            return ' '.join([str(j+1) for j in range(temp,temp+i)])
    return -1

n, l = map(int,input().split())
print(search(n,l))
