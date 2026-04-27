import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
arr = []

for i in range(n):
    arr.insert(lst[i], i+1)

arr.reverse()
print(*arr)