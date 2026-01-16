import sys

n = int(sys.stdin.readline())
res = 0

for i in range(n):
    res += int(sys.stdin.readline())

print(res-(n-1))