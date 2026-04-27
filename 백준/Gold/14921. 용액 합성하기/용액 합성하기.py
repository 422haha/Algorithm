import sys

n = int(sys.stdin.readline().rstrip())
lst = list(map(int, sys.stdin.readline().rstrip().split()))

i = 0
j = n-1
res = 2000000000

while i < j:
    temp = lst[i] + lst[j]
    if abs(res) > abs(temp):
        res = temp
        if res == 0:
            break
    if temp < 0:
        i += 1
    else:
        j -= 1

print(res)