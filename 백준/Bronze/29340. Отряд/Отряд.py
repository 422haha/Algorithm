a = input()
b = input()

print("".join([str(max(int(x), int(y))) for x, y in zip(a, b)]))