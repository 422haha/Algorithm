n, m, k = map(int, input().split())
print(min(min(n//2, m), (n+m-k)//3))