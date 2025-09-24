x, y = map(int, input().split())
n = int(input())
res = x/y

for _ in range(n):
    xi, yi = map(int, input().split())
    temp = xi/yi
    if temp < res:
        res = temp

print(f"{res*1000:.2f}")