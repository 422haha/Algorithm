import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
x = int(sys.stdin.readline())

i = 0
j = n-1
res = 0
while i < j:
    if lst[i] + lst[j] == x:
        j -= 1
        res += 1
    else:
        if lst[i] + lst[j] < x:
            i += 1
        else:
            j -= 1
print(res)