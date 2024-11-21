t = int(input())

for _ in range(t): 
    g,c,e = map(int, input().split())
    if c >= e:
        print(0)
    else:
        if g == 1:
            print(e-c)
        elif g == 2:
            print(3*(e-c))
        elif g == 3:
            print(5*(e-c))