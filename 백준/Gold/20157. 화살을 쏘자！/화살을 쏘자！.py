n = int(input())
gradient = []
num = {}

def gcd(num_1, num_2):
    while num_2 != 0:
        r = num_1 % num_2
        num_1, num_2 = num_2, r
    return abs(num_1)

for i in range(n):
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        continue
    elif x == 0:
        if y > 0:
            gradient.append('+y')
        else:
            gradient.append('-y')
    elif y == 0:
        if x > 0:
            gradient.append('+x')
        else:
            gradient.append('-x')
    else:
        g = gcd(x, y)
        x //= g
        y //= g
        gradient.append((x, y))

for j in gradient:
    if j in num:
        num[j] += 1
    else:
        num[j] = 1

print(max(num.values())) 
