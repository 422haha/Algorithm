import sys

n = int(sys.stdin.readline().rstrip())
res = 0

for i in range(n):
    if i == 0:
        res += n-1
    else:
        res += (n-1-i) * 2

print(res)
for i in range(1, n):
    print(1, i+1)