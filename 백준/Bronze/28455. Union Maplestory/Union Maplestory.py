import sys

n = int(sys.stdin.readline().rstrip())
lst = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
lst.sort(reverse=True)
if len(lst) >= 42:
    lst = lst[:42]

res = 0
for i in lst:
    if i >= 250:
        res += 5
    elif i >= 200:
        res += 4
    elif i >= 140:
        res += 3
    elif i >= 100:
        res += 2
    elif i >= 60:
        res += 1

print(sum(lst), res)