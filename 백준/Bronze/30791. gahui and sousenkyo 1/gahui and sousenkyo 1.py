n, *lst = map(int, input().split())
print(sum(n-i <= 1000 for i in lst))