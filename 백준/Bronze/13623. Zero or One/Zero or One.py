a, b, c = map(int, input().split())

if a != b and a != c and b == c:
    print('A')
elif b != a and b != c and a == c:
    print('B')
elif c != a and c != b and a == b:
    print('C')
else:
    print('*')
