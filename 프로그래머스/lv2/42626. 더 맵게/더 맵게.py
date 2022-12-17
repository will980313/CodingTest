import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while scoville:
        a = heapq.heappop(scoville)
        if a >= K:
            break
            
        if len(scoville) == 0:
            count = -1
            break
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + b*2)
        count+=1
    return count