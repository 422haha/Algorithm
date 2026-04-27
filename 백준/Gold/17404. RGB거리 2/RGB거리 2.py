import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
inf = int(1e9)
res = inf

for i in range(3):
    dp = [[1001] * 3 for _ in range(n)]
    dp[0][i] = arr[0][i]
    for j in range(1, n):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + arr[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + arr[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + arr[j][2]
    dp[-1][i] = inf
    res = min(res, min(dp[-1]))

print(res)