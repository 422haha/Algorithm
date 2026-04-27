n = int(input())
Hexagon = 1

for i in range(n):
    Hexagon += 6*i
    if Hexagon >= n:
        print(i+1)
        break