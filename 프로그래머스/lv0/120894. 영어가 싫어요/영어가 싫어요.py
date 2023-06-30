def solution(numbers):
    answer = ''
    dict_num = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    stack = ''
    for i in numbers:
        stack+=i
        if stack in dict_num.keys():
            answer += str(dict_num[stack])
            stack = ''
    return int(answer)