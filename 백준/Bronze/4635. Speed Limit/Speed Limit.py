while True:
    n = int(input())
    if n == -1:
        break
    res = 0
    time = 0
    for _ in range(n):
        s, t = map(int, input().split())
        res += s*(t-time)
        time = t
    print(res, "miles")