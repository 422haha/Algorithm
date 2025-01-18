a, b, c = sorted(map(int, input().split()))
print(1 if (a+b == c) else 2 if (a*b == c) else 3)