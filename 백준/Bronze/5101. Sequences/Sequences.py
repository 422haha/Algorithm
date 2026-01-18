while True:
    a, b, c = list(map(int, input().split()))
    if a == 0 and b == 0 and c == 0:
        break
    if (c-a)%b == 0 and (c-a)//b >= 0:
        print((c-a)//b+1)
    else:
        print("X")