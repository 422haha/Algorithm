n, m = map(int, input().split())
print(min(n, m)*2+min(abs(n-m), 1))