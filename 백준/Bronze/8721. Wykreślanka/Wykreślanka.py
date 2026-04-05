n = int(input())
lst = list(map(int, input().split()))
res = 0
num = 1
for i in range(n):
    if lst[i] != num:
        res += 1
    else:
        num += 1
print(res)