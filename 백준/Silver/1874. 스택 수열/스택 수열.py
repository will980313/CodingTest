n = int(input())
seq = [int(input()) for _ in range(n)]
stack = [0]
answer = []
count = 1
for c in seq:
    while c != stack[-1]:
        stack.append(count)
        answer.append('+')
        if count > n:
            print('NO')
            count = 0
            break
        count+=1
    else:
        stack.pop()
        answer.append('-')
        continue
    break
if count:
    for i in answer:
        print(i)