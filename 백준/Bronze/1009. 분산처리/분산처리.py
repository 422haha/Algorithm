import sys

t = int(sys.stdin.readline().rstrip())
res = []

for tc in range(1, t+1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a % 10 == 0:
        res.append(10)
    else:
        temp = 4 + b % 4
        temp_str = str(a ** temp)
        res.append(temp_str[-1])

for i in res:
    print(i)