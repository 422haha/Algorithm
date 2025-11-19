t = int(input())
while True:
    n = int(input())
    if n == 0:
        break
    if n%t == 0:
        print(n, "is a multiple of", str(t)+".")
    elif n%t != 0:
        print(n, "is NOT a multiple of", str(t)+".")