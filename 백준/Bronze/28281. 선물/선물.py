n, x = map(int, input().split())
lst = list(map(int, input().split()))

print(min(lst[i]+lst[i+1] for i in range(n-1))*x)