from collections import Counter
def solution(array):
    array = Counter(array).most_common()
    if len(array) > 1 and array[0][1] == array[1][1]:
        return -1
    return array[0][0]