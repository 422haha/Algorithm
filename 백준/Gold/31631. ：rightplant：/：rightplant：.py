import sys

n = int(input())
temp = [1, 2]

for i in range(2, n):
    for j in range(i):
        temp[j] += 1
    idx = i % 4
    if idx % 2 == 0:
        idx = i // 2
    elif idx == 1:
        idx = (i - 1) // 2
    else:
        idx = (i - 1) // 2 + 1
    temp.insert(idx, 1)   # 위치에 맞게 insert

print(*temp)