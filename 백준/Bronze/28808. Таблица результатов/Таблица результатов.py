n, m = map(int, input().split())
print(sum('+' in input() for _ in range(n)))