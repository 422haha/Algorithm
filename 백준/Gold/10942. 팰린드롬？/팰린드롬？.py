import sys

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [[0]*n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1
for i in range(n-1):
    if lst[i] == lst[i+1]:
        dp[i][i+1] = 1
    else:
        dp[i][i+1] = 0

for j in range(n-2):
    for i in range(n-2-j):
        if lst[i] == lst[i+j+2] and dp[i+1][i+j+1] == 1:
            dp[i][i+j+2] = 1

m = int(sys.stdin.readline().rstrip())
for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    print(dp[i-1][j-1])