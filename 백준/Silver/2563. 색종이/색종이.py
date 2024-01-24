n = int(input())
a = [[0]*100 for i in range(100)]

for j in range(n):
    x, y = map(int, input().split())
    for k in range(x, x+10):
        for l in range(y, y+10):
            if 0 <= k < 100 and 0 <= l < 100:
                a[k][l] = 1

sum_a = 0
for m in a:
    sum_a += sum(m)
print(sum_a)