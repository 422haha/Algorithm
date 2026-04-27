import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
lst = [0]*1000001
for _ in range(n):
    s, f = map(int, sys.stdin.readline().rstrip().split())
    for i in range(s, f):
        lst[i] += 1

i = 0
j = 0
temp = 0
flag = 0

while i <= j and j < 1000001:
    if temp == k:
        flag = 1
        break
    elif temp > k:
        temp -= lst[i]
        i += 1
    elif temp < k:
        temp += lst[j]
        j += 1

if flag == 0:
    print(0, 0)
else:
    print(i, j)