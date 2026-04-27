import sys
n = int(sys.stdin.readline())
lst = [0]*10001

for _ in range(n):
    num = int(sys.stdin.readline())
    lst[num] += 1

for i in range(10001):
    if lst[i]:
        for j in range(lst[i]):
            print(i)