import sys

a, b = map(int, sys.stdin.readline().rstrip().split())
n = int(sys.stdin.readline().rstrip())
lst = [int(sys.stdin.readline()) for _ in range(n)]
min_len_s = a

for i in lst:
    if abs(min_len_s - b) > abs(i - b):
        min_len_s = i

if min_len_s == a:
    print(abs(a-b))
else:
    print(abs(min_len_s - b) + 1)