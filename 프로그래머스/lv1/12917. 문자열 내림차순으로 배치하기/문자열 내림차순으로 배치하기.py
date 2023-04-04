def solution(s):
    s = list(s)
    s.sort(reverse = True, key = lambda x: ord(x))
    return ''.join(s)