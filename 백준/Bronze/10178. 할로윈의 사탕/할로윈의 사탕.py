for _ in range(int(input())):
    c, v = map(int, input().split())
    a, b = divmod(c, v)
    print(f"You get {a} piece(s) and your dad gets {b} piece(s).")