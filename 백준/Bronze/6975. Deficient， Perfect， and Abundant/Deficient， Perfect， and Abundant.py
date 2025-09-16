for _ in range(int(input())):
    n = int(input())
    res = 1
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            res += i
            if i*i != n:
                res += n//i
    if res == n:
        print(f"{n} is a perfect number.")
        print()
    elif res < n:
        print(f"{n} is a deficient number.")
        print()
    else:
        print(f"{n} is an abundant number.")
        print()