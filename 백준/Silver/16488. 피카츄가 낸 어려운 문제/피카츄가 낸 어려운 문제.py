import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
print(int(k*n**2))