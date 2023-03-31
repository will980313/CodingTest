def solution(name, yearning, photo):
    def check(nd, x):
        ret = name_dict.get(x)
        if ret is None:
            ret = 0
        return ret
    
    name_dict = {n:i for n, i in zip(name,yearning)}
    
    return [sum(map(lambda x: check(name_dict, x), i)) for i in photo]