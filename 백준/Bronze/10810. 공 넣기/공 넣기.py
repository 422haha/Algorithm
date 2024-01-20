n, m = map(int, input().split())
data = [0] * (n + 1)

for a in range(m):
    i, j, k = map(int, input().split())
    for b in range(i, j+1):
        data[b] = k

for c in range(1, n+1):
    print(data[c], end=' ')