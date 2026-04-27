import sys
import math


n, k = map(int, sys.stdin.readline().rstrip().split())
res = math.comb(n, k)
res %= 10007

print(res)