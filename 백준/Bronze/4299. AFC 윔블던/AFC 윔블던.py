n, m = map(int, input().split())

if n < m or (n+m)%2 or (n-m)%2 == 1:
    print(-1)
else:
    print((n+m)//2, (n-m)//2)