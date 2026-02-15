n = int(input())
num = 1

while True:
    if num == n:
        print(1)
        break
    elif num > n:
        print(0)
        break
    num *= 2