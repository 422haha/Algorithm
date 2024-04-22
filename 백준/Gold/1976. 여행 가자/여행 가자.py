import sys
sys.setrecursionlimit(1000000)


def make_set(n):
    return [i for i in range(n)]


def find_set(x):
    if parents[x] == x:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x > y:
        parents[x] = y
    else:
        parents[y] = x


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
parents = make_set(n)

for i in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(n):
        if temp[j] == 1:
            union(i, j)

temp = list(map(int, sys.stdin.readline().rstrip().split()))
memo = find_set(temp[0]-1)

for i in range(1, m):
    if find_set(temp[i]-1) != memo:
        print('NO')
        sys.exit(0)
print('YES')