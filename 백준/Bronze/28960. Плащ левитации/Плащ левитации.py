h, l, a, b = map(int, input().split())

for i, j in [(a, b), (b, a)]:
    if i/2 <= h and j <= l:
        print("YES")
        break
else:
    print("NO")
