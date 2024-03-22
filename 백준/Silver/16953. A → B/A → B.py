import sys
from collections import deque


def bfs(n):
    dq = deque([(n, 1)])
    visited = {}
    visited[n] = 1
    while dq:
        now, cnt = dq.popleft()
        if now == b:
            return cnt
        temp = [now*2, now*10+1]
        for w in temp:
            if w <= b and w not in visited:
                dq.append((w, cnt + 1))
                visited[w] = 1
    return -1


a, b = map(int, sys.stdin.readline().rstrip().split())
print(bfs(a))