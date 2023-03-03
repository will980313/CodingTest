n, k = map(int,input().split())
len_list = [int(input()) for _ in range(n)]
high = max(len_list)+1
low = 0
while high - low > 1:
    temp = 0
    mid = (high - low) //2 + low
    for i in len_list:
        temp += i//mid
    if temp < k:
        high = mid
    elif temp >= k:
        low = mid
print(low)