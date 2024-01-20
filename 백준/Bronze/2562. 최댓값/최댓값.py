a_list = []
for i in range(9):
    a = int(input())
    a_list.append(a)

max = max(a_list)
print(max)
print(a_list.index(max)+1)