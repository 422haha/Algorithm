x = int(input())
fraction = 0
line = 0
num = 0

for i in range(1, x+1):
    fraction += i
    if fraction >= x:
        line = i
        num = fraction-x
        break

if line % 2 != 1:
    print(f'{line-num}/{num+1}')
else:
    print(f'{num+1}/{line-num}')