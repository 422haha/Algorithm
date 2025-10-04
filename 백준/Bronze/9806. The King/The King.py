_ = int(input())
e = int(input())
lst = list(map(int, input().split()))
res = 0

if e == 2:
    for i in lst:
        res += i**2
else:
    for i in lst:
        if i > 0:
            res += i**e

print(res)