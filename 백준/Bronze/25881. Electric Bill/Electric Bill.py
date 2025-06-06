a, b = map(int, input().split())
for _ in range(int(input())):
    n = int(input())
    print(n, a*min(n, 1000)+b*max(n-1000, 0))