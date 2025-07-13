for _ in range(int(input())):
    n, a, d = map(int, input().split())
    print(n*a+d*(n-1)*n//2)