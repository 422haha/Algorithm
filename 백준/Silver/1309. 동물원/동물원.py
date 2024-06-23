import sys

n = int(sys.stdin.readline().rstrip())
if n == 1:
    print(3)
    sys.exit(0)

dp = [0] * (n+1)
dp[1] = 3
dp[2] = 7
for i in range(3, n+1):
    dp[i] = (2*dp[i-1] + dp[i-2]) % 9901

print(dp[n])