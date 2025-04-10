n, k = map(int, input().split())
lst = list(map(int, input().split()))
res = []

for i in lst:
    p = i*100//n
    if p <= 4:
        res.append(1)
    elif p <= 11:
        res.append(2)
    elif p <= 23:
        res.append(3)
    elif p <= 40:
        res.append(4)
    elif p <= 60:
        res.append(5)
    elif p <= 77:
        res.append(6)
    elif p <= 89:
        res.append(7)
    elif p <= 96:
        res.append(8)
    else:
        res.append(9)

print(*res)
