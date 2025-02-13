for _ in range(int(input())):
    c, p = map(int,input().split())
    if c > 1:
        print(c, p)
        print(c*p-(c-1)*2)
    else:
        print(c, p)
        print(c*p)