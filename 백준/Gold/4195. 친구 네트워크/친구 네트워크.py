import sys
sys.setrecursionlimit(1000000)


def find_set(x):
    if parents[x] != x:
        parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x == y:
        return network[x]
    parents[y] = x
    network[x] += network[y]
    return network[x]


t = int(sys.stdin.readline().rstrip())

for tc in range(1, t+1):
    n = int(sys.stdin.readline().rstrip())
    parents = {}
    network = {}
    res = 0
    for i in range(n):
        x, y = map(str, sys.stdin.readline().rstrip().split())
        if not network.get(x):
            parents[x] = x
            network[x] = 1
        if not network.get(y):
            parents[y] = y
            network[y] = 1
        print(union(x, y))