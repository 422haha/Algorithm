import sys

t = int(sys.stdin.readline().rstrip())

for tc in range(1, t+1):
    lst = list(map(int, sys.stdin.readline().rstrip().split()))
    lst.sort()
    if abs(lst[1]-lst[3]) >= 4:
        print('KIN')
    else:
        print(sum(lst)-max(lst)-min(lst))