k, d = map(int, input().split())
res = 0
i = 1

while d > 0:
    d -= i*k
    res += 1
    i *= 2
if d < 0:
    res -= 1

print(res)