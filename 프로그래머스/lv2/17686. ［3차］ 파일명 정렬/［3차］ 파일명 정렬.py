def solution(files):
    answer = []
    for i, file in enumerate(files):
        head = ''
        number = ''
        tail = ''
        for c in file:
            if not c.isdigit():
                head+=c
            else:
                break
        for c in file[len(head):]:
            if c.isdigit() and len(c) < 5:
                number+=c
            else:
                break        
        tail = file[len(head)+len(number):]
        
        answer.append((tail,head.lower(),0 if number=='' else int(number),i))
    return [files[i[3]] for i in sorted(answer,key = lambda x: (x[1],x[2],x[3]))]