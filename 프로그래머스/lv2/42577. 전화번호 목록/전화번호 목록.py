def solution(phone_book):
    answer = True
    phone_book = set(phone_book)
    for phone_number in phone_book:
        s = ''
        for i in phone_number:
            s+=i
            if s in phone_book and s !=phone_number:
                answer = False

    return answer