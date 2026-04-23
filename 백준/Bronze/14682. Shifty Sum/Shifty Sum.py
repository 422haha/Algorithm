n = int(input())
k = int(input())

res = n
for _ in range(k):
    res *= 10
    res += n
print(res)