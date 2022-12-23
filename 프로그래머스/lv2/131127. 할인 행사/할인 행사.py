from collections import Counter

def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)):
        cnt = Counter(discount[i:i+10])
        for item, num in zip(want, number):
            check = True
            if cnt[item] < num:
                check = False
                break
        if check == True:
            print(i)
            answer += 1
    return answer