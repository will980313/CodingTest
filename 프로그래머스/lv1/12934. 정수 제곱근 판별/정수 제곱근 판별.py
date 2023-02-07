def solution(n):
    if int(n**0.5 * 100 % 100) == 0:
        return int((n**0.5+1)**2)
    return -1