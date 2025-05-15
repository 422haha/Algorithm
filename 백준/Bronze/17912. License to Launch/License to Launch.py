n = int(input())
lst = list(map(int, input().split()))

temp = float('inf')
res = -1

for i in range(n):
    if lst[i] < temp:
        temp = lst[i]
        res = i

print(res)