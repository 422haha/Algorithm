import sys
import math

n, k = map(int, sys.stdin.readline().rstrip().split())
res = math.comb(n-1, k-1)

print(res)