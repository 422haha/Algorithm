import sys

mod = 100999
dp = [0]*2001
dp[0] = 1

for i in range(1, 2001):
    for j in range(2000-i, -1, -1):
        dp[i+j] = (dp[i+j] + dp[j]) % mod

t = int(sys.stdin.readline().rstrip())

for tc in range(1, t+1):
    n = int(sys.stdin.readline().rstrip())
    print(dp[n])