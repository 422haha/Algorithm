n, m = map(int, input().split())
a = []
b = []

for i in range(n):
    a.append(list(map(int, input().split())))
for j in range(n):
    b.append(list(map(int, input().split())))
for k in range(n):
    for l in range(m):
        print(a[k][l]+b[k][l], end=' ')
    print()