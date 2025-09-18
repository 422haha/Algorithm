m, h = map(int, input().split())
n = int(input())

res = 0
for _ in range(n):
    c, b = map(int, input().split())
    res += max(c*m, b*h)

print(res)