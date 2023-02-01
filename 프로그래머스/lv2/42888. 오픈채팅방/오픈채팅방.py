def solution(record):
    answer = []
    dict_name = {i.split()[1]: i.split()[2] for i in record if len(i.split()) == 3}
    for i in record:
        if 'Enter' in i:
            answer.append(f'{dict_name[i.split()[1]]}님이 들어왔습니다.')
        elif 'Leave' in i:
            answer.append(f'{dict_name[i.split()[1]]}님이 나갔습니다.')
    return answer