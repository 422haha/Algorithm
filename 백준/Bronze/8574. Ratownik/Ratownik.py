n, k, x, y = map(int, input().split())
res = 0

for i in range(n):
    xi, yi = map(int, input().split())
    d = ((x-xi)**2+(y-yi)**2)**0.5
    if d > k:
        res += 1

print(res)