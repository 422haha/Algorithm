import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
lst = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
lst.sort(reverse=True)

dp = [0]*(k+1)
dp[0] = 1   # 0을 만드는 경우 1
for i in lst:
    for j in range(i, k+1):
        dp[j] += dp[j-i]

print(dp[k])