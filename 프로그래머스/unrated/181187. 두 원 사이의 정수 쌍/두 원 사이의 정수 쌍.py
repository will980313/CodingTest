import math
def solution(r1, r2):
    answer = 0
    for x in range(1, r2+1):
        if x < r1:
            min_y = math.ceil(math.sqrt(math.pow(r1, 2) - math.pow(x, 2)))
        else:
            min_y = 0
        max_y = math.floor(math.sqrt(math.pow(r2, 2) - math.pow(x, 2)))
        answer+= max_y - min_y +1
    return answer*4