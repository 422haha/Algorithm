import sys
from collections import deque


def bfs(s):
    dq = deque([s])
    num = 1
    visited[s] = num
    num += 1
    while dq:
        t = dq.popleft()
        for i in adjl[t]:
            if visited[i] == 0:
                visited[i] = num
                num += 1
                dq.append(i)


n, m, r = map(int, sys.stdin.readline().rstrip().split())
adjl = [[] for _ in range(n+1)]
for _ in range(m):
    n1, n2 = map(int, sys.stdin.readline().rstrip().split())
    adjl[n1].append(n2)
    adjl[n2].append(n1)
for i in adjl:
    i.sort()
visited = [0] * (n+1)
bfs(r)
for i in range(1, n+1):
    print(visited[i])