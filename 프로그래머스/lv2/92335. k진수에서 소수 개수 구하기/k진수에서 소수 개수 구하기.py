def isprime(n):
    for i in range(2, int(n**(1/2)) +1):
        if n%i ==0:
            return False
    return True


def solution(n, k):
    answer =''
    count = 0
    while n > 0:
        n, mod = divmod(n, k)
        answer += str(mod)
    answer = answer[::-1].split('0')
    for i in answer:
        if len(i) == 0 or i == '1':
            continue
        if isprime(int(i)):
            count+=1
    return count