import sys

n = int(sys.stdin.readline())
arr = [[0]* 1001 for _ in range(1001)]
lst = []
cnt = 0
cnt_lst = []

for i in range(n):
    x, y, w, h = map(int, sys.stdin.readline().rstrip().split())
    lst.append([x, y, w, h])

lst.reverse()

for i in range(n):
    cnt = 0
    x, y, w, h = lst[i]
    for j in range(x, x+w):
        for k in range(y, y+h):
            if arr[j][k] == 0:
                cnt += 1
                arr[j][k] = 1
    cnt_lst.append(cnt)

cnt_lst.reverse()

for i in cnt_lst:
    print(i)