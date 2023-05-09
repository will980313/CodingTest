from collections import Counter
s = input()
n = int(input())
words = [input() for _ in range(n)]
dp = [100 for _ in range(len(s))] + [0] 
for i in range(len(s)):  
    for w in words:
        if Counter(w) == Counter(s[i:i+len(w)]):
            count = 0
            for j in range(len(w)):
                if s[i:i+len(w)][j] != w[j]:
                    count+=1
            dp[i+len(w)-1] = min(dp[i+len(w)-1], dp[i-1]+count)
if dp[len(s)-1] == 100:
    print(-1)
else:
    print(dp[len(s)-1])