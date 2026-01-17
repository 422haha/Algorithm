res = 1

for _ in range(int(input())) :
    x, y = map(int, input().split())
    if res == x :
        res = y
    elif res == y :
        res = x
print(res)