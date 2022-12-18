def solution(s):
    count = 0
    count_z = 0
    while len(s) != 1:
        temp =s.replace("0","")
        count_z+= len(s) - len(temp) 
        num = len(temp)
        s = str(bin(num))[2:]
        count+=1
    return [count,count_z]