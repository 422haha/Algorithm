import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
temp = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0
stress = 0
for a in temp:
    stress += a
    if stress >= m:
        cnt += 1
    if stress < 0:
        stress = 0

print(cnt)