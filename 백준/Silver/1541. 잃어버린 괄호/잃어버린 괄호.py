s = input().split('-')
answer = 0
for i, plus in enumerate(s):
    temp = 0
    for num in plus.split('+'):
        temp+=int(num)
    if i:
        answer -= temp
    else:
        answer += temp
print(answer)