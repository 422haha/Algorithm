a, b, c = open(0).read().split()
print(sum(x == y for x, y in zip(b, c)))