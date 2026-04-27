B, N, M = map(int, input().split())

dct = {name: int(price) for name, price in (input().split() for _ in range(N))}
total = sum(dct[input().strip()] for _ in range(M))

print("acceptable" if total <= B else "unacceptable")