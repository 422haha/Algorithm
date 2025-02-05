n = int(input())
print("short" if -2**15 <= n <= 2**15-1 else "int" if -2**31 <= n <= 2**31-1 else "long long")