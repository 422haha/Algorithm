p, q = map(int, input().split())
a, b = map(int, input().split())
print(min(p, q)*a + max(q-p, 0)*b)