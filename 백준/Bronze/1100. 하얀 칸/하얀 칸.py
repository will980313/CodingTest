count = 0
for i in range(8):
    row = input()
    count += row[i%2::2].count('F')
print(count)