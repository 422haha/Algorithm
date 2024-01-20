n = int(input())
add = 0
data = input()

a = [int(i) for i in data.split(' ')]
v = int(input())

for j in a:
    if j == v:
        add += 1
print(add)