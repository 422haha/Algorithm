import sys
sys.setrecursionlimit(1000000)


def dfs(n):
    for i in arr[n]:
        if visited[i] == 0:
            visited[i] = n  # 방문체크
            dfs(i)


n = int(sys.stdin.readline())
arr = [[] for i in range(n+1)]
visited = [0]*(n+1)         # 방문체크

for i in range(n-1):
    n1, n2 = map(int, sys.stdin.readline().rstrip().split())
    arr[n1].append(n2)
    arr[n2].append(n1)

dfs(1)

for i in range(2, n+1):
    print(visited[i])