def solution(word):
    answer = 0
    dic = ['A','E','I','O','U','']
    make_dic = ''
    while True:
        temp = ''
        if make_dic == word:
            break
        if len(make_dic) != 5:
            temp = make_dic + 'A'
        else:
            for i in range(1,6):
                temp +=  dic[dic.index(make_dic[-i])+1]
                if make_dic[-i] != 'U':
                    temp = make_dic[:-i] + temp[::-1]
                    break
        make_dic = temp
        answer+=1
    return answer

