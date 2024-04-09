import sys

n, score, p = map(int, sys.stdin.readline().rstrip().split())

if n == 0:
    print(1)
    exit(0)

lst = list(map(int, sys.stdin.readline().rstrip().split()))
if n == p and lst[-1] >= score:
    print(-1)
    exit(0)

for i in range(n):
    if lst[i] <= score:
        print(i+1)
        exit(0)

print(n+1)