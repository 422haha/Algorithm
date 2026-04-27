import sys
import math
sys.setrecursionlimit(1000000)


def make_set(n):
    return [i for i in range(n)]


def find_set(x):
    while parents[x] != x:  # 재귀 대신 반복문 사용
        x = parents[x]
    return x


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


n = int(sys.stdin.readline().rstrip())
parents = make_set(n+1)
stars = []
edges = []
res = 0

for i in range(n):
    x, y = map(float, sys.stdin.readline().rstrip().split())
    stars.append((x, y))

for i in range(n-1):
    for j in range(i+1, n):
        edges.append((math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2), i, j))
edges.sort()

for cost, x, y in edges:
    if find_set(x) != find_set(y):
        union(x, y)
        res += cost

print(round(res, 2))