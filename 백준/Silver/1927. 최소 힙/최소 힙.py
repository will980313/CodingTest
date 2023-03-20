import heapq
import sys

n = int(input())
heap = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)