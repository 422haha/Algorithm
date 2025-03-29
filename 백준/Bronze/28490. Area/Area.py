res = 0
for i in range(int(input())):
    h, w = map(int,input().split())
    res = max(res, h*w)

print(res)