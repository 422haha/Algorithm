a, b, c = sorted(map(int, input().split()))

for char in input():
    if char == 'A':
        print(a, end=' ')
    elif char == 'B':
        print(b, end=' ')
    else:
        print(c, end=' ')