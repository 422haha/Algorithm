import sys
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def dfs(i, j, cnt):
    global res
    res = max(res, cnt)
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0 <= ni < r and 0 <= nj < c and arr[ni][nj] not in visited:
            visited.add(arr[ni][nj])
            dfs(ni, nj, cnt+1)
            visited.remove(arr[ni][nj])


r, c = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(r)]
visited = set()
visited.add(arr[0][0])
res = 0
dfs(0, 0, 1)
print(res)