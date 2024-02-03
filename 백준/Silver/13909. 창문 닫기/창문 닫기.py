import sys

n = int(sys.stdin.readline())
cnt = 0
for i in range(1, n+1):
    if i**2 <= n:
        cnt += 1
print(cnt)