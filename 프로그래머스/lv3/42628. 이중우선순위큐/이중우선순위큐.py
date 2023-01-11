import heapq
def solution(operations):
    min_que = []
    max_que = []
    for cmd in operations:
        if cmd[0] =='I':
            heapq.heappush(max_que, -int(cmd[1:]))
            heapq.heappush(min_que, int(cmd[1:]))
        elif cmd == 'D -1' and len(min_que) != 0:
            heapq.heappop(min_que)
            max_que = [-i for i in min_que]
            heapq.heapify(max_que)
        elif cmd == 'D 1' and len(max_que) != 0:
            heapq.heappop(max_que)
            min_que = [-i for i in max_que]
            heapq.heapify(min_que)  
    if len(max_que) == 0:
            heapq.heappush(max_que, 0)
            heapq.heappush(min_que, 0)
    answer = [-heapq.heappop(max_que) ,heapq.heappop(min_que)]
    return answer