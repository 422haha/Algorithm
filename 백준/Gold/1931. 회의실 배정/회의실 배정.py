import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    r, c = map(int, sys.stdin.readline().rstrip().split())
    lst = [r, c]
    arr.append(lst)
arr.sort(key=lambda x:(x[1], x[0]))

now = arr[0][1]
cnt = 1
for i in range(1, n):
    if arr[i][0] >= now:
        cnt += 1
        now = arr[i][1]
print(cnt)