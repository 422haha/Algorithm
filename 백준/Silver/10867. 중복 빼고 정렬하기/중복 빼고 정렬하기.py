import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().rstrip().split()))

lst = list(set(lst))
lst.sort()

print(*lst)