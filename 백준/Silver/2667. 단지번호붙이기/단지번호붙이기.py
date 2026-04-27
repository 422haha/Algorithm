import sys
from collections import deque
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up


def bfs(i, j):
    queue = deque([(i, j)])
    arr[j][i] = 0
    cnt = 1

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and arr[nc][nr]:
                arr[nc][nr] = 0
                queue.append((nr, nc))
                cnt += 1

    return cnt


n = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

res = []

for j in range(n):
    for i in range(n):
        if arr[j][i]:
            res.append(bfs(i, j))

res.sort()
print(len(res))
for cnt in res:
    print(cnt)