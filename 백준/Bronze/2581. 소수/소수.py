m = int(input())
n = int(input())
lst = []

for i in range(m, n+1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        lst.append(i)

if len(lst) > 0:
    print(sum(lst))
    print(lst[0])
else:
    print('-1')