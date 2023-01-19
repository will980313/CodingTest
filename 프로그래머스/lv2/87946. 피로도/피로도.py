import itertools
def solution(k, dungeons):
    answer = -1
    all_list = list(itertools.permutations(dungeons, len(dungeons)))
    for dun in all_list:
        p = k
        for i, dun_2 in enumerate(dun):
            if p - dun_2[1]  <= 0 or p < dun_2[0]:
                
                if answer < i:
                    answer = i
                break
            elif i + 1 == len(dun):
                answer= 1 + i
            p-=dun_2[1]

            
            
    return answer