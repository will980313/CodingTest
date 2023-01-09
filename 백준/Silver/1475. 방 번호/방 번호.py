from collections import Counter
n = input().replace('9', '6')
n = Counter(n)
answer = 0
for i in n:
    if i == '6'and n[i]//2 + n[i]%2 > answer:
        answer = n[i]//2 + n[i]%2
    elif i != '6'and n[i] > answer:
        answer = n[i]
print(answer)
