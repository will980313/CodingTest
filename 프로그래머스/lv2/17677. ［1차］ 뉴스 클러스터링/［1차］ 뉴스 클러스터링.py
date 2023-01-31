import re
def solution(str1, str2):
    str1 = [(str1[i]+str1[i+1]).lower() for i in range(len(str1)-1) if (str1[i]+str1[i+1]).isalpha()]
    str2 = [(str2[i]+str2[i+1]).lower() for i in range(len(str2)-1) if (str2[i]+str2[i+1]).isalpha()]
    set1 = []
    set2 = []
    for s in str1:
        if s in str2:
            set1.append(s)
            set2.append(s)
            str2.remove(s)
        else:
            set2.append(s)
    if len(str2):
        set2 += str2
    if len(set1) == 0 and len(set2) == 0:
        return 65536
    if len(set1) == 0:
        return 0
    return int(len(set1) / len(set2) * 65536)