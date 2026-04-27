import sys

n = int(sys.stdin.readline().rstrip())
i = 1   # start
j = n   # end

while i < j:
    temp = (i + j)//2
    if temp**2 == n:
        print(temp)
        sys.exit(0)
    if temp**2 > n:
        j = temp
    else:
        i = temp