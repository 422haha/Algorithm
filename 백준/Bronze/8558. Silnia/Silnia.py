n = int(input())

if n >= 5:
    print(0)
else:
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    print(factorial%10)