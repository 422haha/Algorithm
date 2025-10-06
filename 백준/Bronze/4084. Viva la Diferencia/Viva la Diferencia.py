while True:
    a, b, c, d = list(map(int, input().split()))
    if a == b == c == d == 0:
        break
    res = 0
    while not (a == b and b == c and c == d):
        res += 1
        temp = a
        a = abs(a-b)
        b = abs(b-c)
        c = abs(c-d)
        d = abs(d-temp)
    print(res)