while True:
    t1, t2 = map(int, input().split())
    if t1 == 0 & t2 == 0:
        break
    print(int(t1/t2), t1%t2, "/", t2)