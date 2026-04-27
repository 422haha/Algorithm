import sys
# sys.stdin = open('input.txt')
from collections import deque


def dfs(m, d):
    if m-1 > -1:
        if magnet[m-1][2] != magnet[m][6] and not visited[m-1]:
            visited[m-1] = d
            dfs(m-1, -d)
    if m+1 < 4:
        if magnet[m][2] != magnet[m+1][6] and not visited[m+1]:
            visited[m+1] = d
            dfs(m+1, -d)


magnet = []
for i in range(4):
    magnet.append(deque(map(int, sys.stdin.readline().rstrip())))
k = int(sys.stdin.readline().rstrip())
for _ in range(k):
    m, d = map(int, sys.stdin.readline().rstrip().split())
    m -= 1
    visited = [0] * 4
    visited[m] = d
    dfs(m, -d)
    for i in range(4):
        magnet[i].rotate(visited[i])
res = 0
for i in range(4):
    res += magnet[i][0]*2**i
print(res)