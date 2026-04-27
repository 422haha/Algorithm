n = int(input())
d = int(input())

if n % 4 == 0:
    if n % 100 == 0:
        if n % 400 == 0:
            print(30)
        else:
            print(29)
    else:
        print(30)
else:
    print(29)