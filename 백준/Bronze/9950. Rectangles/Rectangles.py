while True:
    try:
        l, w, a = map(int, input().split())
    except:
        break
    if l == 0 and w == 0 and a == 0:
        break
    if l == 0:
        l = a//w
    elif w == 0:
        w = a//l
    else:
        a = l*w
    print(f"{l} {w} {a}")