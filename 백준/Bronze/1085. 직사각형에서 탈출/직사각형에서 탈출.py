x, y, h, w = map(int,input().split())
print(min([x, y, abs(h-x), abs(w-y)]))

