from heapq import heappop, heappush
from collections import Counter

def solution(k, tangerine):
    answer = []
    bigest = max(tangerine)
    tangerine = Counter(tangerine)
    for i in range(1, bigest+1):
        heappush(answer, -tangerine[i])
    for i in range(bigest):
        k += heappop(answer)
        if k <= 0:
            return i+1