import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
num = str(a*b*c)
cnt = [0]*10

for i in num:
    cnt[int(i)] += 1

for i in cnt:
    print(i)