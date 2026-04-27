import sys
n = int(sys.stdin.readline())
lst = []
for i in range(n):
    [x, y] = map(int, sys.stdin.readline().rstrip().split())
    lst.append([x, y])
lst.sort()

for j in lst:
    print(j[0], j[1])