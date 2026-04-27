import sys

n = int(sys.stdin.readline())
f = [0] * (n+1)
if n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    f[1] = 0
    f[2] = 1
    for i in range(3, n+1):
        f[i] = f[i-1] + 1
        if (i-1)//6 != i//6:
            f[i] = min(f[i], f[i//2]+1, f[i//3]+1)
        elif (i-1)//3 != i//3:
            f[i] = min(f[i], f[i//3]+1)
        elif (i-1)//2 != i//2:
            f[i] = min(f[i], f[i//2]+1)
    print(f[n])