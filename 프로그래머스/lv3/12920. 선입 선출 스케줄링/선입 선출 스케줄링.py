def solution(n, cores):
    left = 1
    right = max(cores) * n
    n-=len(cores)
    
    while left < right:
        mid = (left + right) //2
        temp = 0
        for c in cores:
            temp+= mid//c
        if temp >= n:
            right = mid
            continue
        left = mid+1
    
    for c in cores:
        n -= (left-1) // c
    
    for i, c in enumerate(cores):
        if left%c == 0:
            n-=1
        if n == 0:
            return i+1
        