import sys

cnt = 0
arr = [[0]*100 for _ in range(100)]

for i in range(4):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    for j in range(x1, x2):
        for k in range(y1, y2):
            if arr[j][k] == 0:
                cnt += 1
                arr[j][k] = 1

print(cnt)