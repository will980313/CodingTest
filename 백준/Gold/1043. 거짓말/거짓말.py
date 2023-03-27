import sys
from collections import deque
n, m = map(int,sys.stdin.readline().split())
know = deque(list(map(int, sys.stdin.readline().split()))[1:])
know_dict = {i+1:False for i in range(n) }
for i in know:
    know_dict[i] = True
party = []
answer = 0
for _ in range(m):
    party.append(list(map(int, sys.stdin.readline().split()))[1:])
while know:
    temp = know.popleft()
    for p in party:
        if temp in p:
            for i in p:
                if know_dict[i] == False:
                    know.append(i)
                    know_dict[i] = True
for p in party:
    for i in p:
        if know_dict[i]:
            break
    else:
        answer+=1
print(answer)