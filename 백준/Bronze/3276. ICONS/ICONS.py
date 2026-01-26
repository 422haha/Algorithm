n = int(input())
i = 1
j = 1

while True:
    if i*j >= n:
        break
    else:
        if i > j:
            j += 1
        else:
            i += 1

print(i, j)