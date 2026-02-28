lst = list(map(int, input().split()))
res = 0
for i in lst:
    if i > 0:
        res += 1
print(res)