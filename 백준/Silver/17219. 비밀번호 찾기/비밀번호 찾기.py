n,m = map(int,input().split())

pass_dict = {}
for _ in range(n):
    temp = input().split()
    pass_dict[temp[0]] = temp[1]
for _ in range(m):
    print(pass_dict[input()])