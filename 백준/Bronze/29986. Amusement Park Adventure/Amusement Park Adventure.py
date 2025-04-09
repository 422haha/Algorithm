n, h = map(int, input().split())
lst = list(map(int, input().split()))

print(sum(1 for i in lst if i <= h))