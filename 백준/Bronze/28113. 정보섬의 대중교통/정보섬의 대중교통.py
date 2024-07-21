n, a, b = map(int, input().split())

if b >= n:
    if b == a:
        print("Anything")
    elif b > a:
        print("Bus")
    else:
        print("Subway")
else:
    print("Bus")