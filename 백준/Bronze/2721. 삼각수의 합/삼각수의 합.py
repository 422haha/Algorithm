for _ in range(int(input())):
    n = int(input())
    w = 0
    for k in range(1, n+1):
        t = (k+1)*(k+2)//2
        w += k*t
    print(w)