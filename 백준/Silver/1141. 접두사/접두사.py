n = int(input())
word = [input() for _ in range(n)]
word =list(set(word))
answer = 0
for i, i_word in enumerate(word):
    for j, j_word in enumerate(word):
        if i == j or len(i_word) > len(j_word):
            continue
        if i_word == j_word[:len(i_word)]:
            break
    else:
        answer+=1
print(answer)