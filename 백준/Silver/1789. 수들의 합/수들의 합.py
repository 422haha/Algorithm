import sys

n = int(sys.stdin.readline())
res = 0
temp = 0

for i in range(1, n+1):
    temp += i
    res = i
    if temp > n:
        res -= 1
        break

print(res)