import sys

n = int(sys.stdin.readline())
cnt = 0
for i in range(n):
    for j in range(n):
        if i != j:
            cnt += 1
print(cnt)