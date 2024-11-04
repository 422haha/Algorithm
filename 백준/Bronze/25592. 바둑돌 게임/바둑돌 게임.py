n = int(input())

temp = 1
while True:
    n -= temp
    if n < 0:
        if temp%2 != 0:
            print(abs(n))
        else:
            print(0)
        break
    temp += 1