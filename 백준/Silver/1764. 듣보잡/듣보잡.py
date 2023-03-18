n,m = map(int,input().split())

a_list = [input() for _ in range(n)]
b_list = [input() for _ in range(m)]
answer = list(set(a_list) & set(b_list))
print(len(answer))
answer.sort()
for i in answer:
    print(i)