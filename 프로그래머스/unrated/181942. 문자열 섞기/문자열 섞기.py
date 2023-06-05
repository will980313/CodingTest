def solution(str1, str2):
    return ''.join([i+j for i, j in zip(str1, str2)])