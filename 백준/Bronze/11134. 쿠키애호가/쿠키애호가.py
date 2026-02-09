for _ in range(int(input())):
    n, c = map(int, input().split())
    if n%c == 0:
        print(n//c)
    else:
        print(n//c+1)