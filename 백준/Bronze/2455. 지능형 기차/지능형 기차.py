temp = 0
res = 0

for _ in range(4):
    out, inn = map(int, input().split())
    temp -= out
    temp += inn
    if temp > res:
        res = temp

print(res)