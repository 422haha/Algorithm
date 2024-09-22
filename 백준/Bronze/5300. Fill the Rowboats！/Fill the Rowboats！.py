n = int(input())

for i in range(1, n+1):
    print(i, end=' ')
    if not i%6:
        print('Go!', end=' ')
if n%6:
    print('Go!')