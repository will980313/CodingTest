def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    i = -1
    j = 0
    while len(people) > i+j+1:
        i+=1
        temp = limit
        temp -= people[i]
        if temp >= people[-(j+1)]:
            j+=1
        answer+=1
    return answer