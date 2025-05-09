x = input()
visited = set()

while x not in visited:
    visited.add(x)
    first_digit = int(x[0])
    length = len(x)
    x = str(first_digit*length)

print("FA")