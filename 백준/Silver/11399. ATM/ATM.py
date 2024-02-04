import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
lst = sorted(lst)
sum = 0
for i in range(len(lst)):
    sum += (len(lst)-i) * lst[i]
print(sum)