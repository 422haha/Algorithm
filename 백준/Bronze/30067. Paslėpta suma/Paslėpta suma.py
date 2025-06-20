lst = [int(input()) for _ in range(10)]
print(next(n for n in lst if sum(lst)-n == n))