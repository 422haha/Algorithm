import sys

t = int(sys.stdin.readline())
f = [0]*11
f[1] = 1
f[2] = 2
f[3] = 4
for i in range(4, 11):
    f[i] = f[i-1] + f[i-2] + f[i-3]

for tc in range(1, t+1):
    n = int(sys.stdin.readline())
    print(f[n])