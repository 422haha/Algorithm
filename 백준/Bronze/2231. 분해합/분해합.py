n = int(input())

for i in range(1, n+1):
    place_num = sum(map(int, str(i)))
    if place_num + i == n:
        print(i)
        break
    if i == n:
        print(0)