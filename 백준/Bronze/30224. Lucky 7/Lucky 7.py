n = int(input())

if '7' not in str(n):
    if n % 7 != 0:
        print(0)
    else:
        print(1)
else:
    if n % 7 != 0:
        print(2)
    else:
        print(3)