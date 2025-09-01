while True:
    b, t, a = input().split()
    b = int(b)
    a = int(a)
    if b == 0 and t == 'W' and a == 0:
        break
    if t == 'W':
        if b-a < -200:
            print('Not allowed')
        else:
            print(b-a)
    elif t == 'D':
        print(b+a)