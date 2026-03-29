n, h, w = map(int, input().split())
for _ in range(n):
    print('NO' if h**2+w**2 < int(input())**2 else 'YES')