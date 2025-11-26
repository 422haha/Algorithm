n = int(input())
res = 0
for a in range(1, 501):
    for b in range(1, a+1):
        if a*a == b*b+n:
            res += 1
print(res)