n, x = map(int, input().split())
data = input()
a = [int(i) for i in data.split(' ')]

for j in a:
    if j < x:
        print(j, end=' ')