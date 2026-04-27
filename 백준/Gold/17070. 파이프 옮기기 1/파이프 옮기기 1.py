import sys


def dfs(i, j, pipe):
    global res
    if i == n-1 and j == n-1:
        res += 1
        return
    if pipe == 0:
        if j < n-1 and arr[i][j+1] == 0:
            dfs(i, j+1, 0)
        if i < n-1 and j < n-1 and arr[i+1][j+1] == 0 and arr[i+1][j] == 0 and arr[i][j+1] == 0:
            dfs(i+1, j+1, 2)
    elif pipe == 1:
        if i < n-1 and arr[i+1][j] == 0:
            dfs(i+1, j, 1)
        if i < n-1 and j < n-1 and arr[i+1][j+1] == 0 and arr[i+1][j] == 0 and arr[i][j+1] == 0:
            dfs(i+1, j+1, 2)
    elif pipe == 2:
        if j < n-1 and arr[i][j+1] == 0:
            dfs(i, j+1, 0)
        if i < n-1 and arr[i+1][j] == 0:
            dfs(i+1, j, 1)
        if i < n-1 and j < n-1 and arr[i+1][j+1] == 0 and arr[i+1][j] == 0 and arr[i][j+1] == 0:
            dfs(i+1, j+1, 2)


n = int(input())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
res = 0
dfs(0, 1, 0)
print(res)