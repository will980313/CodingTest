def solution(players, callings):
    players_dict1 = {p:i for i, p in enumerate(players)}
    players_dict2 = {i:p for i, p in enumerate(players)}
    for p in callings:
        players_dict2[players_dict1[p]], players_dict2[players_dict1[p]-1] = players_dict2[players_dict1[p]-1], players_dict2[players_dict1[p]]
        players_dict1[players_dict2[players_dict1[p]]] = players_dict1[p]
        players_dict1[p] = players_dict1[p] - 1
    return [players_dict2[i] for i in range(len(players))]