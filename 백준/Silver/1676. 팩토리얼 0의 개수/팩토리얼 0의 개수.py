def factorial(n):
    if n == 0:
        return 1
    return factorial(n-1)*n

n = int(input())
num = factorial(n)
answer = 0
for i in str(num)[::-1]:
    if i == '0':
        answer+=1
    else:
        break
print(answer)