import sys
n = int(sys.stdin.readline())
lst_n = []
for _ in range(n):
    lst_n.append(sys.stdin.readline().rstrip())

lst = list(set(lst_n))
lst.sort()
lst.sort(key=len)

for i in lst:
    print(i)