import sys
sys.setrecursionlimit(10**6)

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def dfs(ci, cj):
    if ci == n-1 and cj == m-1: # 목적지 도달
        return 1
    if dp[ci][cj] != -1:        # 방문한 곳이라면 그 위치에서의 경우의 수 리턴
        return dp[ci][cj]
    cnt = 0
    for d in range(4):          # 방문하지 않은 곳이라면 경우의수 구하기
        ni = ci + di[d]
        nj = cj + dj[d]
        if 0 <= ni < n and 0 <= nj < m and arr[ci][cj] > arr[ni][nj]:   # 벽 체크, 다음 지점이 높이가 더 낮은지 확인
            cnt += dfs(ni, nj)
    dp[ci][cj] = cnt
    return dp[ci][cj]


n, m = map(int, sys.stdin.readline().rstrip().split())  # 세로 n, 가로 m
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

dp = [[-1]*m for _ in range(n)]
res = dfs(0, 0)

print(res)