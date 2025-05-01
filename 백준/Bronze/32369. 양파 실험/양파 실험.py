n, a, b = map(int, input().split())

praise = 1
blame = 1

for _ in range(n):
    praise += a
    blame += b

    if blame > praise:
        praise, blame = blame, praise
    elif blame == praise:
        blame -= 1

print(praise, blame)