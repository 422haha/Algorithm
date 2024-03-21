import sys


def dfs(n, level):
    if visited[n]:
        return 0
    visited[n] = 1
    for neighbor in arr[n]:
        if not visited[neighbor]:
            level += dfs(neighbor, 1)
    return level


t = int(sys.stdin.readline().rstrip())  # 테스트 케이스의 개수 입력

for tc in range(t):
    n = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())
    arr = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    root = 0
    depth = 0  # 트리의 깊이
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        arr[a].append(b)
        arr[b].append(a)
        if not root:
            root = a
    if m != n - 1:
        print("graph")
        continue
    if dfs(root, 1) == n:
        print("tree")
    else:
        print("graph")