import sys

n = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = 0

for i in n:
    cnt += i**2

print(cnt % 10)