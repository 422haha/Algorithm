import sys

# 입력을 받습니다.
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

# DP 배열 초기화
dp = [[0] * (m + 1) for _ in range(n + 1)]

# DP 배열 채우기
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = arr[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]

# 질의 수를 입력받습니다.
k = int(sys.stdin.readline().rstrip())

# 각 질의에 대해 부분합을 계산하여 출력
for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    result = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
    print(result)
