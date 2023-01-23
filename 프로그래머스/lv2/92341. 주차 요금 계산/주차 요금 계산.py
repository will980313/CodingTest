import math
def solution(fees, records):
    answer = []
    num_dic = {i.split()[1]:[] for i in records} 
    for record in records:
        record = record.split()
        record[0] = record[0].split(':')
        num_dic[record[1]].append(int(record[0][0]) * 60 + int(record[0][1]))

    for i in num_dic:
        if len(num_dic[i])%2 == 1:
            num_dic[i].append(1439)
        temp = 0
        for j in range(0,len(num_dic[i]),2):
            temp += num_dic[i][j-1] - num_dic[i][j]
        num_dic[i].append(temp)
    
    for i in sorted(num_dic):
        temp = num_dic[i][-1]
        temp -= fees[0]
        if temp <= 0:
            answer.append(fees[1]) 
            continue  
        answer.append(math.ceil(temp/fees[2])*fees[3] + fees[1]) 
    print(num_dic)
    return answer