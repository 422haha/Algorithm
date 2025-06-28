import math

n = int(input())
lst = list(map(int, input().split()))

res = 0
for i in lst:
    if i%2 != 0:
        i += 1
    res += math.ceil(i/2)

print(res)