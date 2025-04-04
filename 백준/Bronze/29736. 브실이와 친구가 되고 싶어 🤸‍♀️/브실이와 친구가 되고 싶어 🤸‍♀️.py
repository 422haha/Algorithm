a, b = map(int, input().split())
k, x = map(int, input().split())
res = len([i for i in range(a, b+1) if (k-x <= i <= k+x)])

print(res if res != 0 else 'IMPOSSIBLE')