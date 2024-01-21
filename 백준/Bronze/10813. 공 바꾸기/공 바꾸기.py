n, m = map(int, input().split())
data = [0]
for num in range(1, n+1):
    data += [num]

for a in range(m):
    temp = 0
    i, j = map(int, input().split())
    temp = data[i]
    data[i] = data[j]
    data[j] = temp

for b in range(1, n+1):
    print(data[b], end=' ')