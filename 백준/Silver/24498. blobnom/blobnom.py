import sys

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [0]*n

if n == 1:
    print(lst[0])
    sys.exit(0)

res = 0
for i in range(1, n-1):
    dp[i] = lst[i] + min(lst[i-1], lst[i+1])
    res = max(res, dp[i])

res = max(res, lst[0])
res = max(res, lst[-1])

print(res)