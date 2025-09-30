n = int(input())
res = 0

for _ in range(n):
    s, a = map(int, input().split())
    res += a%s

print(res)