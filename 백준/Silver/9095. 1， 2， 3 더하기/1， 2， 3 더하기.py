import sys
n = int(sys.stdin.readline())
answer = [1, 2, 4]
for i in range(9):
    answer.append(sum(answer[i:i+3]))
for _ in range(n):
    num = int(sys.stdin.readline())
    print(answer[num-1])