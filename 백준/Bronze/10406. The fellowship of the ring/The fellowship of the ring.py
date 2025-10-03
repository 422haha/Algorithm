w, n, p = map(int, input().split())
lst = list(map(int, input().split()))

res = 0

for h in lst:
    if w <= h <= n:
        res += 1

print(res)