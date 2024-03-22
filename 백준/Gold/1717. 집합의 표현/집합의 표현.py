import sys
sys.setrecursionlimit(100000)


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])  # 부모 노드를 재귀적으로 찾음 (경로 압축)
    return parents[x]


def union(x, y):        # 두 집합을 합치는 함수
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


n, m = map(int, sys.stdin.readline().rstrip().split())
parents = [i for i in range(n+1)]
for i in range(m):
    x, a, b = map(int, sys.stdin.readline().rstrip().split())
    if x == 0:            # 합집합 연산 수행
        union(a, b)
    elif x == 1:          # 부모 확인
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')