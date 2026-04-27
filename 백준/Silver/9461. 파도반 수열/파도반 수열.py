import sys

t = int(sys.stdin.readline())
f = [0] * 101
f[1] = 1
f[2] = 1
f[3] = 1
f[4] = 2
f[5] = 2
for i in range(6, 101):
    f[i] = f[i - 1] + f[i - 5]

for tc in range(1, t+1):
    n = int(sys.stdin.readline())
    print(f[n])

