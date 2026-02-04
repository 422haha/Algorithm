for _ in range(int(input())):
    n, d, a, b, f = map(float, input().split())
    t = d/(a+b)*f
    print("%d %.6f"%(n, t))