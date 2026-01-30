for _ in range(int(input())):
    n, m = map(int, input().split())
    res = 0
    for a in range(1, n-1):
        for b in range(a+1, n):
            if (a**2+b**2+m)%(a*b) == 0:
                res += 1
    print(res)