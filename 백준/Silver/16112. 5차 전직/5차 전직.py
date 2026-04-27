import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
sum_ = 0
lst.sort()

for i in range(k):
    sum_ -= lst[i] * (k - i)

for i in lst:
    sum_ += i * k

print(sum_)