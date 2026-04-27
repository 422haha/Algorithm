n, t = map(int, input().split())
res = 0
temp = 1

for _ in range(t):
    res += temp
    if res == 2*n:
        temp = -1
    if res == 1:
        temp = 1
print(res)