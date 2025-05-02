n = int(input())
lst = [int(input()) for _ in range(n)]

m = int(input())
res = 0
for _ in range(m):
    i = int(input())
    res += lst[i-1]

print(res)