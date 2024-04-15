import sys


def make_set(n):
    return [i for i in range(n)]


def find_set(x):
    if parents[x] != x:
        parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


n, m = map(int, sys.stdin.readline().rstrip().split())

parents = make_set(n+1)

graph = []
for _ in range(m):
    graph.append([int(i) for i in sys.stdin.readline().rstrip().split()])

graph.sort(key=lambda x: x[2])

res = 0
max_ = 0

for edge in graph:
    s, f, d = edge
    if find_set(s) != find_set(f):
        union(s, f)
        res += d
        max_ = max(d, max_)

print(res - max_)