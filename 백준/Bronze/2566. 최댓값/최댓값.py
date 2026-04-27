a = []
max_num = 0
max_row = 0
max_column = 0

for i in range(1, 10):
    temp = list(map(int, input().split()))
    if max(temp) >= max_num:
        max_num = max(temp)
        max_row = i
        max_column = temp.index(max_num) + 1
    a.append(temp)

print(max_num)
print(max_row, max_column)