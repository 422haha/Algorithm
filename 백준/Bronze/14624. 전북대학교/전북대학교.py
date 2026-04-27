n = int(input())
d = n // 2

if n % 2 != 0:
    print('*' * n)
    print(' ' * d + '*')
    for i in range(d):
        print(' ' * (d - i - 1) + '*' + ' ' * (i * 2 + 1) + '*')
else:
    print('I LOVE CBNU')