num = int(input())
str_list = list(input())
for _ in range(num - 1):
    temp = input()
    for i, alp in enumerate(temp):
        if str_list[i] != alp:
            str_list[i] = '?'
print(''.join(s for s in str_list))
