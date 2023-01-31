from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    for city in cities:
        city = city.lower()
        if city in cache:
            answer+=1
            temp_que = deque()
            for _ in range(len(cache)):
                temp = cache.popleft()
                if city == temp:
                    continue
                temp_que.append(temp)
            temp_que.append(city)
            cache = temp_que
        else:
            answer+=5
            cache.append(city)
        if cacheSize < len(cache) and len(cache) != 0:
            cache.popleft()  
    return answer