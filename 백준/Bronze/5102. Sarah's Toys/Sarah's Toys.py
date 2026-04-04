while True:
    a, b = map(int, input().split())
    if a == 0 and a == b:
        break
    x = (a-b)//2
    if (a-b)%2 and x >= 1:
        y = 1
        if x >= 1:
            x -= 1
    else:
        y = 0
    print(x, y)