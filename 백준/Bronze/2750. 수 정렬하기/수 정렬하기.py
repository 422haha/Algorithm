import sys
n = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(n)]
lst.sort()

for i in lst:
    print(i)