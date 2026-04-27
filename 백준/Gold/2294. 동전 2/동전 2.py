import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
lst = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
lst.sort(reverse=True)

dp = [10001]*(k+1)
dp[0] = 0   # 0을 만드는 경우 0
for i in lst:
    for j in range(i, k+1):
        dp[j] = min(dp[j], dp[j-i]+1)

res = dp[k]
if res == 10001:
    print(-1)
else:
    print(res)