quadrant = [0]*4
axis = 0
for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        axis += 1
    elif x > 0 and y > 0:
        quadrant[0] += 1
    elif x < 0 and y > 0:
        quadrant[1] += 1
    elif x < 0 and y < 0:
        quadrant[2] += 1
    else:
        quadrant[3] += 1

print("Q1:", quadrant[0])
print("Q2:", quadrant[1])
print("Q3:", quadrant[2])
print("Q4:", quadrant[3])
print("AXIS:", axis)