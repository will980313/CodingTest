n, m = map(int, input().split())
temp = 9999
pack = []
single = []
for _ in range(m):
    line_pack, line_single = map(int, input().split())
    pack.append(line_pack)
    single.append(line_single)
min_pack = min(pack)
min_single = min(single)
if min_pack > min_single * 6:
    print(min_single * n)
elif min_single * (n%6) < min_pack:
    print(min_pack * (n//6) + min_single * (n%6))
else:
    print(min_pack * (n//6+1))