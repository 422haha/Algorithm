n = int(input())

res = 0
for i in range(6):
    for j in range(i, 6):
        if i+j == n:
            res += 1

print(res)