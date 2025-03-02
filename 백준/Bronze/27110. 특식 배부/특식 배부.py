n = int(input())
a, b, c = list(map(int, input().split()))

print(min(a, n)+min(b, n)+min(c, n))