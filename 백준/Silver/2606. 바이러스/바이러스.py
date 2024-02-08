import sys
def dfs():
    stack = []
    visited[1] = 1
    cnt = 0
    n = 1
    while True:
        for w in adjl[n]:
            if visited[w] == 0:
                stack.append(n)
                n = w
                visited[n] = 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break
    for i in visited:
        if i == 1:
            cnt += 1
    return cnt


v = int(sys.stdin.readline())
e = int(sys.stdin.readline())
adjl = [[] for _ in range(v+1)]
visited = [0] * (v+1)
for i in range(e):
    r, c = map(int, sys.stdin.readline().rstrip().split())
    adjl[r].append(c)
    adjl[c].append(r)
print(dfs()-1)