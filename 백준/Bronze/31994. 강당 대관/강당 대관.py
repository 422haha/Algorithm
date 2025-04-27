max_count = -1
winner = ""

for _ in range(7):
    name, count = input().split()
    count = int(count)
    if count > max_count:
        max_count = count
        winner = name

print(winner)