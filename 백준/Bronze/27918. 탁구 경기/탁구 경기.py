x = 0
y = 0

for i in range(int(input())):
    s = input()

    if abs(x-y) < 2:
        if s == 'D':
            x += 1
        else:
            y += 1

print("{}:{}".format(x, y))