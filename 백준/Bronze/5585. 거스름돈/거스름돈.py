import sys

n = 1000-int(sys.stdin.readline().rstrip())
temp = [500, 100, 50, 10, 5, 1]
cnt = 0

for i in temp:
    cnt += n // i
    n %= i

print(cnt)