from heapq import heappush, heappop

def solution(n, k, enemy):
    answer = 0
    heap = [0]
    for rnd in enemy:
        heappush(heap, -rnd)
        if n < rnd:
            if k != 0:
                n += -heappop(heap)
                k -= 1
            else:
                break
        answer+=1
        n -= rnd
    return answer


