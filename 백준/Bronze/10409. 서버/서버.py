n, t = map(int, input().split())
lst = list(map(int, input().split()))

res = 0
for i in lst:
    if i <= t:
        t -= i
        res += 1
    else:
        break

print(res)