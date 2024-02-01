import sys

n = int(sys.stdin.readline())
dct = {}

for i in range(n):
    n, m = sys.stdin.readline().rstrip().split()
    if m == 'enter':
        dct[n] = m
    else:
        del dct[n]

dct = sorted(dct.keys(), reverse=True)

for i in dct:
    print(i)