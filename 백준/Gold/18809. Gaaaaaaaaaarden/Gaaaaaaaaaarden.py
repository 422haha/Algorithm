import sys
from collections import deque
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def bfs(temp):
    dq = deque()
    cnt = 0
    visited = [[0] * m for _ in range(n)]   # visited 배열 초기화
    for i in range(len(node)):
        if temp[i] == 0:
            continue
        ni, nj = node[i]
        visited[ni][nj] = temp[i]
        dq.append([ni, nj])
    while dq:
        ni, nj = dq.popleft()
        if visited[ni][nj] == inf:  # 이미 방문한 경우 건너뜀
            continue
        for d in range(4):
            wi = ni + di[d]
            wj = nj + dj[d]
            if 0 <= wi < n and 0 <= wj < m:
                if arr[wi][wj] == 0 or visited[wi][wj] == inf:  # 이미 방문한 경우 건너뜀
                    continue
                if visited[wi][wj] == 0:                        # 방문한 적 없는 경우
                    if visited[ni][nj] < 0:
                        visited[wi][wj] = visited[ni][nj] - 1
                        dq.append([wi, wj])
                    else:
                        visited[wi][wj] = visited[ni][nj] + 1
                        dq.append([wi, wj])
                else:                                           # 이미 방문한 경우 꽃 체크
                    if visited[ni][nj] < 0:
                        if visited[wi][wj] + visited[ni][nj] - 1 == 0:
                            cnt += 1
                            visited[wi][wj] = inf
                    else:
                        if visited[wi][wj] + visited[ni][nj] + 1 == 0:
                            cnt += 1
                            visited[wi][wj] = inf
    return cnt


def dfs(level, green, red, temp):
    global res
    if level == len(node):
        if green == g and red == r:
            res = max(res, bfs(temp))
        return
    dfs(level+1, green+1, red, temp + [1])  # 초록색 배양액을 뿌리는 경우
    dfs(level+1, green, red+1, temp + [-1]) # 빨간색 배양액을 뿌리는 경우
    dfs(level+1, green, red, temp + [0])    # 배양액을 뿌리지 않는 경우


n, m, g, r = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
inf = int(1e9)
node = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:  # 배양액을 뿌릴 수 있는 위치 찾기
            node.append([i, j])
res = 0
dfs(0, 0, 0, [])
print(res)