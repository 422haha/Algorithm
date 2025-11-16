n = int(input())
m = int(input())
flag = 0

res = m
for _ in range(n) :
    a, b = map(int, input().split())
    m = m+a-b
    if m < 0 :
        flag = 1
    elif m > res :
        res = m
if flag == 0 :
    print(res)
else :
    print(0)