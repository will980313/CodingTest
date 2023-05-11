n = int(input())
nums = list(map(int, input().split()))
s = int(input())

for i in range(n-1):
    temp_max = max(nums[i:i+s+1])
    if s ==0:
        break
    if nums[i] < temp_max:
        temp_index = nums.index(temp_max)
        nums.insert(i,nums[temp_index])
        del nums[temp_index+1]
        s-= temp_index - i
print(' '.join(map(str,nums)))