import sys

n = int(sys.stdin.readline().rstrip())
building_list = list(map(int, sys.stdin.readline().rstrip().split()))
lst = [0]*n
inf = -1e9

for i in range(n-1):
  max_slope = inf
  for j in range(i+1, n):
    slope = (building_list[j]-building_list[i])/(j-i)
    if slope <= max_slope:
      continue
    max_slope = max(max_slope, slope)
    lst[i] += 1
    lst[j] += 1

res = max(lst)
print(res)