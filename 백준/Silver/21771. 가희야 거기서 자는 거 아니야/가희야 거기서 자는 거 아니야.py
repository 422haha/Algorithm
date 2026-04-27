import sys

r, c = map(int, sys.stdin.readline().rstrip().split())
gr, gc, pr, pc = map(int, sys.stdin.readline().rstrip().split())

arr = []
res = pr * pc
for _ in range(r):
    temp = list(sys.stdin.readline().rstrip())
    res -= temp.count('P')
    arr.append(temp)

if res:
    print(1)
else:
    print(0)