import sys
import math

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
day = list(map(int, sys.stdin.readline().rstrip().split()))

arr = []
for l, d in zip(lst, day):
    arr.append([l, d])

arr.sort(key=lambda x: (x[1], x[0]))

max_ = arr[0][0]    # 구간 최댓값
now = arr[0][1]     # 기준점
res = 0
cnt = 0

for i in range(n):
    if now > arr[i][0]:
        cnt = math.ceil((now - arr[i][0]) / 30)
        arr[i][0] += cnt * 30
        res += cnt
    max_ = max(max_, arr[i][0])
    if i+1 < n and (arr[i][1] != arr[i+1][1]):
        now = max(max_, arr[i+1][1])

print(res)