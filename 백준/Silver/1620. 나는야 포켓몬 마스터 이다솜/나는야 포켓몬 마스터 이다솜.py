import sys
input = sys.stdin.readline
n,m = map(int,input().split())
poket_dict = {}
for i in range(1,n+1):
    temp = input()[:-1]
    poket_dict[temp] = str(i)
    poket_dict[str(i)] = temp
for _ in range(m):
    print(poket_dict[input()[:-1]])