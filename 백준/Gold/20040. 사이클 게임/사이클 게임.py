import sys
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


n, m = map(int, sys.stdin.readline().rstrip().split())
parents = make_set(n)

for i in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    if find_set(x) == find_set(y):
        print(i+1)
        sys.exit(0)
    union(x, y)

print(0)
sys.exit(0)