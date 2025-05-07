n = int(input())

flag = False
for i in range(2, 10):
    for j in range(1, 10):
        if n == i or n == j or n == i * j:
            flag = True
            break
    if flag:
        break

print(1 if flag else 0)