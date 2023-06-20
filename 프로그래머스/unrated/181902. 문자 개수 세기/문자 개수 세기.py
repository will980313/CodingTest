def solution(my_string):
    answer = {chr(i): 0 for i in range(65,123)}
    for i in range(91,97):
        del answer[chr(i)]
    for c in my_string:
        answer[c]+=1
    return list(answer.values())