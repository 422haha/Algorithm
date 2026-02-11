for _ in range(int(input())):
    n, d = map(int, input().split())
    res = 0
    for i in range(n):
        v, f, c = map(int, input().split())
        if v*f/c >= d:
            res += 1
    print(res)