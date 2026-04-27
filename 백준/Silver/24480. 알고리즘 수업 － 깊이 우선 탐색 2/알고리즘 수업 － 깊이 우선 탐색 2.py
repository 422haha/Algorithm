import sys
sys.setrecursionlimit(100000)


def dfs(n):
    global num
    visited[n] = num
    num += 1
    for w in adjl[n]:
        if visited[w] == 0:
            dfs(w)


n, m, r = map(int, sys.stdin.readline().rstrip().split())
adjl = [[] for _ in range(n+1)]
for _ in range(m):
    n1, n2 = map(int, sys.stdin.readline().rstrip().split())
    adjl[n1].append(n2)
    adjl[n2].append(n1)
for i in adjl:
    i.sort(reverse=True)
num = 1
visited = [0] * (n+1)
dfs(r)
for i in range(1, n+1):
    print(visited[i])