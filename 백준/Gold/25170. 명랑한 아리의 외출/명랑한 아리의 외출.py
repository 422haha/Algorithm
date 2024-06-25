import sys

n, m, t = map(int, sys.stdin.readline().rstrip().split())

work = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
time = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

dp = [[[-1]*(t+1) for _ in range(m)] for _ in range(n)]
dp[0][0][0] = 0

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue

        for k in range(1, t+1):
            if i - 1 >= 0 and k - 1 >= 0:
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1])
                w = k - 1 - time[i][j]
                if w >= 0 and dp[i-1][j][w] != -1:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][w] + work[i][j])
            if j - 1 >= 0 and k - 1 >= 0:
                dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k-1])
                w = k - 1 - time[i][j]
                if w >= 0 and dp[i][j - 1][w] != -1:
                    dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][w] + work[i][j])
            if i - 1 >= 0 and j - 1 >= 0 and k - 1 >= 0:
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][k-1])
                w = k - 1 - time[i][j]
                if w >= 0 and dp[i - 1][j - 1][w] != -1:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][w] + work[i][j])

print(max(dp[n-1][m-1]))