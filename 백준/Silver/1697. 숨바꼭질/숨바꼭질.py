import sys
from collections import deque


def bfs(n):
    dq = deque([(n, 0)])
    visited = {}
    visited[n] = 1
    while dq:
        now, cnt = dq.popleft()
        if now == k:
            return cnt
        temp = [now + 1, now - 1, now * 2]
        for w in temp:
            if 0 <= w <= 100000 and w not in visited:
                dq.append((w, cnt + 1))
                visited[w] = 1
    return -1


n, k = map(int, sys.stdin.readline().rstrip().split())
print(bfs(n))