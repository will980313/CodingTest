import string
def solution(msg):
    answer = []
    LZW_dict = {c:i+1 for i, c in enumerate(string.ascii_uppercase)}
    i = 0
    msg +='!'
    while i < len(msg) - 1:
        for j in range(i+1, len(msg)+1):
            if msg[i:j] not in LZW_dict:
                LZW_dict[msg[i:j]] = len(LZW_dict)+1
                answer.append(LZW_dict[msg[i:j-1]])
                i += len(msg[i:j-1])
                break
    return answer