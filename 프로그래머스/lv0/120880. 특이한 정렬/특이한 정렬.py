def solution(numlist, n):
    numlist.sort(key= lambda x : (abs(x-n), -x))
    return numlist