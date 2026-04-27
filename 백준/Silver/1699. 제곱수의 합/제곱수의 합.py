import sys

n = int(sys.stdin.readline().rstrip())
dp = list(range(n+1))

for i in range(1, n+1):
    for j in range(1, i):
        if j**2 > i:
            break
        if dp[i] > dp[i-j*j] + 1:
            dp[i] = dp[i-j*j] + 1

print(dp[n])