n = input()
print(n[-1] if n in ("123456789"[:i+1] for i in range(9)) else -1)