a1, a2, a3 = (int(input()) for _ in range(3))
print(2*min(a2+2*a3, a1+a3, 2*a1+a2))