lst = [1, 0, 0, 2]
for i in input():
    if i == 'A':
        lst[0], lst[1] = lst[1], lst[0]
    elif i == 'B':
        lst[0], lst[2] = lst[2], lst[0]
    elif i == 'C':
        lst[0], lst[3] = lst[3], lst[0]
    elif i == 'D':
        lst[1], lst[2] = lst[2], lst[1]
    elif i == 'E':
        lst[1], lst[3] = lst[3], lst[1]
    else:
        lst[2], lst[3] = lst[3], lst[2]
print(lst.index(1)+1)
print(lst.index(2)+1)