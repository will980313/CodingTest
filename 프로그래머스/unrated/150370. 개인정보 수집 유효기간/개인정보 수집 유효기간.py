import datetime
def solution(today, terms, privacies):
    answer = []
    dict_term = {}
    today = datetime.datetime.strptime(today,'%Y.%m.%d')
    for i in terms:
        cat,month = i.split()
        dict_term[cat] = int(month)
    for i, n in enumerate(privacies):
        date, cat = n.split()
        Y,M,D = date.split('.')
        M = int(M)+dict_term[cat]
        Y = int(Y)
        D = int(D)
        if M >12:
            Y = Y + M//12
            M = M%12
            if M ==0:
                M = 12
                Y-=1
        datime_date = datetime.datetime(Y,M,D)
        diff = today - datime_date
        if diff.days >= 0:
            answer.append(i+1)
    return answer