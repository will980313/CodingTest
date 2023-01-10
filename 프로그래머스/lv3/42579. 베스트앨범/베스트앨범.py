def solution(genres, plays):
    temp_dict = {i: [0] for i in list(set(genres))}
    for i, (gen, p) in enumerate(zip(genres, plays)):
        temp_dict[gen][0] += p
        temp_dict[gen].append([i,p])
    temp_dict = sorted(temp_dict.items(), key = lambda x: x[1][0], reverse = True)
    answer = []
    for song in temp_dict:
        temp = sorted(song[1][1:], key= lambda x: x[1], reverse = True)
        answer.append(temp[0][0])
        if len(temp) > 1:
            answer.append(temp[1][0])
    return answer