import sys

t = int(sys.stdin.readline().rstrip())

for tc in range(1, t+1) :
    n, m = map(int, sys.stdin.readline().rstrip().split())
    visited = [0]*(n+1)
    temp = []

    for i in range(m) :
        a, b = map(int, sys.stdin.readline().rstrip().split())
        temp.append((a, b))
    temp.sort(key=lambda x: x[1])

    res = 0
    while temp :
        a, b = temp.pop(0)
        for i in range(a, b+1):
            if not visited[i]:
                visited[i] = True
                res += 1
                break

    print(res)