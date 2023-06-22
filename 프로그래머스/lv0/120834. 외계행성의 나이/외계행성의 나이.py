def solution(age):
    answer = [chr(i) for i in range(97, 123)]
    return ''.join([answer[int(i)] for i in str(age)])