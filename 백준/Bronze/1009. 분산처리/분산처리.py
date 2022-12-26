num = int(input())
for _ in range(num):
    a,b = map(int, input().split())
    temp_list = []
    cont = 0
    while True:
        cont += 1
        temp = a**cont%10
        if temp in temp_list:
             cont -= 1
             break
        temp_list.append(temp)
    answer = temp_list[(b-1)%cont]
    if answer == 0:
       answer = 10
    print(answer)