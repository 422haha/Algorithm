import sys


def dfs(x):
    visited_dfs[x] = 1
    print(x, end=' ')
    for w in adjl[x]:
        if visited_dfs[w] == 0:
            dfs(w)


def bfs(x):
    q = [x]
    visited = [0]*(n+1)
    visited[x] = 1
    while q:
        t = q.pop(0)
        print(t, end=' ')
        for w in adjl[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = 1


n, m, v = map(int, sys.stdin.readline().rstrip().split())
adjl = [[] for _ in range(n+1)]
for i in range(m):
    n1, n2 = map(int, sys.stdin.readline().rstrip().split())
    adjl[n1].append(n2)
    adjl[n2].append(n1)
for i in adjl:
    i.sort()
visited_dfs = [0] * (n+1)
dfs(v)
print()
bfs(v)